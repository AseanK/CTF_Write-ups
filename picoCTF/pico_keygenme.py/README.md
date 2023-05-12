# Description
`keygenme.trial.py`

**tags: Reverse Engineering**

## Notes
- Global Variables
```username_trial = "GOUGH"
bUsername_trial = b"GOUGH"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```

- Looks like we only have to get `key_part_dynamic1_trial` to solve<br>
- Snippets for the `key_part_dynamic1_trial` :

```def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False



        return True
```
- It fisrt checks if the length of `key_full_template_trial` matches
- It checks if the `key_part_static1_trial` matches after
- Iterates HashSet for the key_part_dynamic1_trial
- Indexes are in following order: <br>
`45362718`

## Reverse Engineering

```import hashlib
from cryptography.fernet import Fernet
import base64

username_trial = b"GOUGH"

ans = ""

orders = [4,5,3,6,2,7,1,8]

for i in orders:
	ans += hashlib.sha256(username_trial).hexdigest()[i]
print(ans)
```

**Flag found: f911a486**
<br>
- Complete flah would be ``picoCTF{1n_7h3_|<3y_of_f911a486``
<br>
Total time spent: ~ 30 minutes