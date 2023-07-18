<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

require_once __DIR__ . '/PHPMailer/PHPMailer/src/Exception.php';
require_once __DIR__ . '/PHPMailer/PHPMailer/src/PHPMailer.php';
require_once __DIR__ . '/PHPMailer/PHPMailer/src/SMTP.php';

$mail = new PHPMailer(true);

$mail->SMTPDebug = 0;
$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->SMTPAuth = true;
$mail->SMTPSecure = "ssl";
$mail->Port = 465;

$mail->mailer = "smtp";

$mail->Username = 'malleswar.gangarapu@gmail.com';
$mail->Password = 'muetcwkeltluhjzb';

// Sender and recipient address
$mail->SetFrom('malleswar.gangarapu@gmail.com', 'Malleswar');
$mail->addAddress('gangarapumalleswar429@gmail.com', 'gangarapu');
// $mail->addReplyTo('ADD-REPLY-TO-EMAIL', 'ADD-REPLY-TO-NAME');

// Setting the subject and body
$mail->IsHTML(true);
$mail->Subject = "Send email from localhost using PHP";
$mail->Body = 'Hi hello how are you!';

if ($mail->send()) {
    echo "Email is sent successfully.";
} else {
    echo "Error in sending an email. Mailer Error: {$mail->ErrorInfo}";
}
?>
