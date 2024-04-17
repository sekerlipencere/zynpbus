<?php
// Gelen veriyi kontrol edelim
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // POST isteğinden gelen veriyi alalım ve ilk 6 karakterini alalım
    $post_veri = substr(file_get_contents("php://input"), 0, 6);

    // Kaydedilecek dosya adı ve yolunu belirleyelim
    $dosya_yolu = "post_verileri.txt";

    // Dosyayı temizleyelim (içeriğini silelim)
    file_put_contents($dosya_yolu, "");

    // Veriyi dosyaya ekleyelim (append)
    file_put_contents($dosya_yolu, $post_veri . PHP_EOL, FILE_APPEND);

    // Başarılı mesajı gönderelim
    echo "Post isteği başarıyla kaydedildi.";
} else {
    // Hatalı istek mesajı gönderelim
    echo "Hatalı istek!";
}
?>