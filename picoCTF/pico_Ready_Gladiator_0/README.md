# Description

Can you make a CoreWars warrior that always loses, no ties?\
Your opponent is the Imp. The source is available `here`./
If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:\
`nc saturn.picoctf.net 54286 < imp.red`

## Notes

- Downloaded the file

`nc saturn.picoctf.net 54286 < imp.red`
```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 0
Ties: 100
Try again. Your warrior (warrior 1) must lose all rounds, no ties.
```

Contant of the `imp.red` file
```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```

- Changed `mov` to `0, 0` and saved the file

`nc saturn.picoctf.net 54286 < imp.red`
```
;redcode
;name Imp Ex
;assert 1
mov 0, 0
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mov 0, 0
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
You did it!
picoCTF{h3r0_t0_z3r0_4m1r1gh7_f1e207c4}
```

**Flag found: picoCTF{h3r0_t0_z3r0_4m1r1gh7_f1e207c4}**
