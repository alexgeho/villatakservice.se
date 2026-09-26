<?php
// Kontaktformulär för villatakservice.se – skickar e-post till info@villatakservice.se
// Ingen tredjepartstjänst. Kräver att PHP mail() är aktiverat på hostingen.

// Formulärsidor vi får skicka tillbaka till (vitlista – aldrig fri redirect).
$retur = (($_POST['retur'] ?? '') === 'offert-dalarna.html') ? 'offert-dalarna.html' : 'kontakt.html';

// Bara POST tillåtet
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Location: kontakt.html');
    exit;
}

// Honeypot: bottar fyller ofta i dolda fält -> låtsas att allt gick bra
if (!empty($_POST['website'])) {
    header('Location: tack.html');
    exit;
}

// Tidsfälla: main.js sätter ts (ms) när sidan laddas. Ifyllt och skickat på
// under 3 s = bot. Saknas ts (JS avstängt) släpps förfrågan igenom som förut.
$ts = (int)($_POST['ts'] ?? 0);
if ($ts > 0 && (microtime(true) * 1000 - $ts) < 3000) {
    header('Location: tack.html');
    exit;
}

// Enkel rate-limit per IP: max 5 förfrågningar per timme.
$ip = $_SERVER['REMOTE_ADDR'] ?? '';
$rlFile = sys_get_temp_dir() . '/vts_rl_' . md5($ip);
$now = time();
$hits = array();
if (is_readable($rlFile)) {
    $hits = array_filter(array_map('intval', explode(',', (string)@file_get_contents($rlFile))),
        function ($t) use ($now) { return $t > $now - 3600; });
}
if (count($hits) >= 5) {
    header('Location: ' . $retur . '?fel=2#form');
    exit;
}
$hits[] = $now;
@file_put_contents($rlFile, implode(',', $hits), LOCK_EX);

// Ta bort radbrytningar (skydd mot header-injection) och trimma
function clean($v) {
    return trim(str_replace(array("\r", "\n", "%0a", "%0d", "%0A", "%0D"), '', (string)$v));
}

$namn      = clean($_POST['namn'] ?? '');
$telefon   = clean($_POST['telefon'] ?? '');
$epost     = clean($_POST['epost'] ?? '');
$tjanst    = clean($_POST['tjanst'] ?? '');
$ort       = clean($_POST['ort'] ?? '');
$meddelande = trim($_POST['meddelande'] ?? '');
$gdpr      = isset($_POST['gdpr']);

// Validering
$errors = array();
if ($namn === '') { $errors[] = 'namn'; }
if ($telefon === '' && $epost === '') { $errors[] = 'kontakt'; }
if ($epost !== '' && !filter_var($epost, FILTER_VALIDATE_EMAIL)) { $errors[] = 'epost'; }
if ($meddelande === '') { $errors[] = 'meddelande'; }
if (!$gdpr) { $errors[] = 'gdpr'; }

if (!empty($errors)) {
    header('Location: ' . $retur . '?fel=1#form');
    exit;
}

// Begränsa längd (enkelt skydd)
$meddelande = mb_substr($meddelande, 0, 5000);

$to      = 'info@villatakservice.se';
$from    = 'info@villatakservice.se'; // finns som brevlåda på servern -> pålitlig lokal leverans
$subject = 'Ny offertförfrågan från villatakservice.se';

$body  = "Ny förfrågan via kontaktformuläret på villatakservice.se\n";
$body .= "-----------------------------------------------------\n\n";
$body .= "Namn:       $namn\n";
$body .= "Telefon:    $telefon\n";
$body .= "E-post:     $epost\n";
$body .= "Tjänst:     $tjanst\n";
if ($ort !== '') {
    $body .= "Ort:        $ort\n";
}
$body .= "Formulär:   $retur\n\n";
$body .= "Meddelande:\n$meddelande\n";

// Spara varje lead UTANFÖR webbroten innan mejlet skickas, så att inget går
// förlorat om mail() fallerar. En rad JSON per förfrågan, en fil per månad.
$leadDir = dirname(__DIR__) . '/leads';
if (!is_dir($leadDir)) {
    @mkdir($leadDir, 0700, true);
}
if (is_dir($leadDir) && is_writable($leadDir)) {
    $row = array('tid' => date('c'), 'namn' => $namn, 'telefon' => $telefon, 'epost' => $epost,
        'tjanst' => $tjanst, 'ort' => $ort, 'formular' => $retur, 'meddelande' => $meddelande);
    @file_put_contents($leadDir . '/leads-' . date('Y-m') . '.jsonl',
        json_encode($row, JSON_UNESCAPED_UNICODE) . "\n", FILE_APPEND | LOCK_EX);
}

$headers  = "From: Villatakservice <$from>\r\n";
if ($epost !== '') {
    $headers .= "Reply-To: $epost\r\n";
}
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

$subjectEncoded = '=?UTF-8?B?' . base64_encode($subject) . '?=';

$sent = @mail($to, $subjectEncoded, $body, $headers, '-f' . $from);

if ($sent) {
    header('Location: tack.html');
} else {
    header('Location: ' . $retur . '?fel=2#form');
}
exit;
