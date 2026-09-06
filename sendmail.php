<?php
// Kontaktformulär för villatakservice.se – skickar e-post till info@villatakservice.se
// Ingen tredjepartstjänst. Kräver att PHP mail() är aktiverat på hostingen.

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

// Ta bort radbrytningar (skydd mot header-injection) och trimma
function clean($v) {
    return trim(str_replace(array("\r", "\n", "%0a", "%0d", "%0A", "%0D"), '', (string)$v));
}

$namn      = clean($_POST['namn'] ?? '');
$telefon   = clean($_POST['telefon'] ?? '');
$epost     = clean($_POST['epost'] ?? '');
$tjanst    = clean($_POST['tjanst'] ?? '');
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
    header('Location: kontakt.html?fel=1#form');
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
$body .= "Tjänst:     $tjanst\n\n";
$body .= "Meddelande:\n$meddelande\n";

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
    header('Location: kontakt.html?fel=2#form');
}
exit;
