# Mass Assignment

The name of the puzzle is in reference to the vulnerability.

```php
$_SESSION = $_POST;
if($username === "ted") {
    $_SESSION['role'] = "admin";
}
```

The entire session is set to the entire POST, so if we include `&role=admin`, our role gets set to "admin", revealing the flag.
