

List (and optionally clean) failed s3 multipart uploads

```
$ python listfaileduploads.py  -h
Usage: listfaileduploads.py [options]

Options:
  -h, --help            show this help message and exit
  --clean               
  --printoldonly        
  --olderthandays=OLDERTHANDAYS
  --verbose=VERBOSE     
```

Run with no arguments will produce a list of all multipart uploads.


example output:

```
default days 7 days, 0:00:00
<MultiPartUpload data1/2gb/BanlTRLPoeCzSPWtsRwWCkRuWbVPOIAGFbmHlSEOriQCwrymtPNbhLwRghrAAGJEfkDCTobvbnfZBqMlZQQLWDKwGCGwmxlBHSqNRdpTEQiZIXXoXuRxMIoipwwZmxUs>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:29.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data1/2gb/qjExPllGqfMzvNghpfwCQObBJDaSkVEsSPcKjSTunXjSUQYBZUQhHwatYGiQBzUXQEvRDbmPjRPGUhgRPGBUWvzOGhLMgeJMHvePirHrbItrrzwIbMXxOPQlwpeqpGQg>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:27.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data2/2gb/gqXfIvONwVhoYXWdtbTHRHDsRDzzDMESXJfoEiKyTezHzaLxPwhBridFWzJwUbOnXkLtcbGclXtUospoZCrLzYzuywLOGlRFZBXGReGoVAbNfterCpgaKqqYKrkkfPbe>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:27.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data2/2gb/sIwWRrcciSMaPrfWsrtSbySIeElqILsCRFKNZdWszEJGbKInIcKagyCdVGPDgPfFoofeHfdzNjIBbDzoVTVCXHySdhndoHhHMpDNZWvfUBQitnxGyWpZWiDSiIVWTXzN>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:27.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data3/2gb/RlsazGbBPpbHDMDMosqTxKCvFIbxKqVbRUJxfDedzovjVvyuuiOfyxTtjiGPbUPyxBscKaXhKtgGEgimDqlMieeZxdlVjQRKnFufWiKopUHcPhDSQBHuCMRnDUHsKVUj>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:27.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data3/2gb/XivezpZvJYaaGoSTryRDjlDDQXjWQcpQtjPswQFwMPmNBOGmAAWCMtIsHeaLsxEAGMWdibmJhjdFaWJmcYifKOjWpLZWlIpOpnmRKPIriAwAbZlFcIDtjYyUNZzsaFOG>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:27.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data4/2gb/VofkqjcbxufnLLqqcWCQhNarmaqaPNTxJzMJjKmavjOMnKovDivdnpQvvPgxDmjfCnacEmtjEGBVpYFLDYEbWNYuqsIQpfMoscKIXiOYtgGdyOTGahtscjZvrCuHBQLy>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:30.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data4/2gb/lVTfSiJrtvOzIyXCowKbiFcJgAqnnrBxuPDTdcMzXItxCvqcylhPZzqHrxHqQdRfCuiYLMqisBrLjfJaraNvhNRHnThcxHHXNVsoOkUXXTthwoeaIKJnDTwOCROgvQEo>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:28.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 4:41:03.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 4:40:13.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 4:37:51.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 3:48:39.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 3:47:58.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 3:47:29.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 3:40:28.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 2:13:12.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload largefile/data1/2gb_4/aaoDGAzAxSiDEzkhaPQSqIbWoCyUvJBGBFHgTqcBaSrboCpuRrWoTTDXcXFAaucVrFDwSKpeWLxZsuQrWYfKiigkpXFQtWZTFDNPUnpWUYojDQtgxwtAEFpxHIiUZhsq>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 10 days, 9:18:19.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload largefile/scratch/jason/bar/en.xml>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
not cleaning, youngest upload part ( 4:02:42.519087 ) was before 7 days, 0:00:00


<MultiPartUpload data1/2gb/IkQMhADWKZJBJVerKeAPwmHumccRYUCGvWnvLCpHOTvtVZuZbsCzjJFEHbwdkcIVjLbqKcrFjzrnXZNiSiJyGGBJfoBiVItfKSXSJdClcFRegitMEgpjeVwbniRWiaRo>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:13:08.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data1/2gb/LOeUprnJxFeHxEXVNedupwjUTVXBMiXnQSaeKYaObsDmBPEvLfyFNlMTtlQrAsTMNDhXBqWzVYjCjvirIiTTVzpFTRDistzJScTpcxJXaZfXcJnMKExbmxnFFayBKMQP>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:56:23.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data1/2gb/gqudcAXxNTXRQdgJVqaKMKMXkqRtWealQIugAJAuGHBOVyBFHudWNxSozDUwtQVpPbHGIyurktCEDmwWiIqSXSxEGnvGyNxxbkziFYJFnqEIpsZlvNKpaEvyvAeARsdl>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:53.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data1/2gb/mwoHnLNYkLUlCzbRHVgQaYmVOSUaNNUOuQRRmNYdlATorWWQiWVLzfXcySIDReWxjaBcbVgRgdHUhqdciAcyNjZOKdDWOJLMMdwwUrYPmgnJczJOUbmMbnpmoSwQbxkw>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:57.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data1/2gb/uxljMzxfyJqpgDwXxlOvENAfssEtAVlKbzDkrxVXLfsCpdOlRJQjQtpKdMAhngirOXUxkDvDmHpEMIPGikfTgodsiBRqCTqAznIxajuhLMyDACsQSLLzxXLVlMviCtxr>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:56:21.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data2/2gb/ERyNPANEnjXvAYEpVORgVHXCIxvSGFicsCqxTHwflRdHPLXNqYJEIrMXsBohWpKcjFDcWBFYEoiOrAzQuEYshouCgLtaJYsaonvhhYZzHVoCwPXGKGbZZCFgoTPKzgww>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:56:23.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data2/2gb/FRolciVigQXRAXmbxcmZgiKmaMBQAGbICtRZaBafLfQQctRoBLtBlNdJXvaQIQXuZouKZDShvhnBbmUASCIgfhgunKjexIvtrjdfZrYSBWPsciecBbGoCmEwDdiBWpiK>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:57.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data2/2gb/FzpxoTnKsRCspOLduRQUDnZQMwCcRaUhZlVXSGsanOZIqSvAntzWqNjaDsZEHMWTOvYIbWHWzozDVQrygoZMfXYihfIppSWyuzwSzSSqnxOdmUEqWDmnftQSiTUnDHKR>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:58:35.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data2/2gb/IHyGUyDlexfFyJCjjdEjmZsbNuEmhSxLBbeaNeUocXwZNQdLelDIWzxVdhcFVmLfCMwHrbSByAgeZEDFhBxZpMZxbsXjvgUdTgiygpbZYhdbZnVOeEpKIoCOBkbFrHkV>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:06:33.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data2/2gb/fsKOgZMjQBQHpnojDUIQIRpvzyAoTpkJbATGbTDjWujpunRCptMAgtbLFdNocyhDKoIkAZCSOKhSkVkSvAdZmblLrMptETZyIEcWsOtweGlSYFbrxGVAjHzbKiDpvyIV>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:32.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data2/2gb/sQRpMgFFxgrLwenpxfjLYsLKDqRubLZkgynglzZxGNHPoTueilJvCIQPUksBYmqkQrXrJFzSMfqkMKAHTPjKlwdVEviSLJWAiTeQOaxkLQEjZAmnJmOLduLjOWsiaFfq>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:11:43.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data3/2gb/DTPMSMcRIzNkWSZsBZaGVUaZowCluWrUycyxagvUEGTmJZnVRIMHoqzyrLXXcabOemXKPvcqKqUNaiAOoayMyNPuEBbDJkZkuAYKQlhZPyATajrRHIjialHmqQwwRuyS>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:57:10.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data3/2gb/QQOgLNTDNtzczUPoeiIztDtytyMnMNWtJOhUxBoSkgfEjbgKVltLKESvNsnWihhlraoguLdezcZNmOjRifAYxCGEmdjWqZhpvUcZElLBoHLUvNfFtItKIrOOueJRJQBp>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:09:40.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data3/2gb/VAUzwAcqtJYBgGhyjeXnyAKOnLXhzHJBZXNIEqtDuLTsMtdBFlQTBknDbWfRdonIzRcWYDVkZHPaJFYYRMxUzDVAwikkQnoWBkJSsaGYiKjyKeKiGRfbACbvQEpnRgTY>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:06:11.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data3/2gb/isdwyOBqnrfjNFejJYWCwBwWctmOBFcvVssYIvJEBRSWmSFBJiiYiWsFTAnXzCUqSnuYnXDmTHDcfPodwXvJvCCWFgXjAEnZoLxBCoZngWRtnqgYsdnzroQkuEeNTlJb>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:33.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data3/2gb/sbAiLNrIjHHFjeqYFfZLPrpGPCnVMZXtfJgtOuzeJdLSyiTxlAtWmQaiJtXIZDTdCryxgjBtsQbwHXQAPAnqPIpaGQKGwcEWgkRJyFioLgroFkDiFcSaKPBrevNHKVQF>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:56:50.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data4/2gb/CBsdQvVAnBGdlaPzeiUWnQRCKBtwgZnJPRkZiZNasFxJlunWuwjmOhXMhZrvjGusiZjVzpoUKBhWPZrfCBhDidBNmLwRsxbkbAVrfPeYklPwwAfaayPUcTDDrVuzjZJn>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:30.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data4/2gb/DzAVuYTTZlWIYSqAGeEanOLfCIAcXuqaueJivawTuzZUpRdLmRIHcXdjmiHIystjzoMVHbyNHgwRrOJffYpOEFCuWVeRfEWELRIULPqRRBGlRgvmJAPGVEuRafvFzeDz>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:30.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data4/2gb/OZbRrpupPsqaLWYvQyLoBMVwDeCkYNNYoreNfnKeskCYCnqEcyKhSovqkukHzyJtjjumgLLoISFVTfJcFCcOizfgsswmceRxEUASDrhxyzNQzCDOFcSyNeUBfKmHcYut>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:29.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data4/2gb/ciQtWbkfRzMEbrNqagvzCOcEHJHabQIkFsfnZuBWrsSyyniIHPcBmegHsVQooqEianhhMEDasBBuVCEXZkAuBoxkKEvmagBfMKkTjFiuYtMpdROlVKMvYvZTWbzvajhr>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:56:23.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data4/2gb/qsofBpDgRJCZJakUjXRBGvjULEEraFYsAztCwZmGujzEURwABMTodgkEPtNWixLzScyYOgFLRvpPrPSQeOCTUHJgnJKgVwTQZlhUFxEKZeRuVcZDYbdBrstitayTfAsn>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:09:35.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag


<MultiPartUpload data4/2gb/sRLFVDhuZOLzDXzdQycUewHSQaYZSxEHBCExGLVoItrrLtUcYaTnNMwwqGhYLEyBkWFwgGGevzKznmJudTPAAUDolGIsRwPvJMqxHJsKxYgGgierzqBnVpxXnFfjBJez>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:56:23.519087 ) is more than 7 days, 0:00:00 ago, would be cleaned with --clean flag




sum bytes of all uploads 76702547968 ( 71  gb)
sum bytes of uploads older than 7 days, 0:00:00  is  67181477888 ( 62  gb)
```


When run with --clean option all parts older than 7 days (the default) are cleaned up, freeing 62gb:


```
default days 7 days, 0:00:00
<MultiPartUpload data1/2gb/BanlTRLPoeCzSPWtsRwWCkRuWbVPOIAGFbmHlSEOriQCwrymtPNbhLwRghrAAGJEfkDCTobvbnfZBqMlZQQLWDKwGCGwmxlBHSqNRdpTEQiZIXXoXuRxMIoipwwZmxUs>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:48.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data1/2gb/qjExPllGqfMzvNghpfwCQObBJDaSkVEsSPcKjSTunXjSUQYBZUQhHwatYGiQBzUXQEvRDbmPjRPGUhgRPGBUWvzOGhLMgeJMHvePirHrbItrrzwIbMXxOPQlwpeqpGQg>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:46.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data2/2gb/gqXfIvONwVhoYXWdtbTHRHDsRDzzDMESXJfoEiKyTezHzaLxPwhBridFWzJwUbOnXkLtcbGclXtUospoZCrLzYzuywLOGlRFZBXGReGoVAbNfterCpgaKqqYKrkkfPbe>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:46.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data2/2gb/sIwWRrcciSMaPrfWsrtSbySIeElqILsCRFKNZdWszEJGbKInIcKagyCdVGPDgPfFoofeHfdzNjIBbDzoVTVCXHySdhndoHhHMpDNZWvfUBQitnxGyWpZWiDSiIVWTXzN>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:46.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data3/2gb/RlsazGbBPpbHDMDMosqTxKCvFIbxKqVbRUJxfDedzovjVvyuuiOfyxTtjiGPbUPyxBscKaXhKtgGEgimDqlMieeZxdlVjQRKnFufWiKopUHcPhDSQBHuCMRnDUHsKVUj>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:46.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data3/2gb/XivezpZvJYaaGoSTryRDjlDDQXjWQcpQtjPswQFwMPmNBOGmAAWCMtIsHeaLsxEAGMWdibmJhjdFaWJmcYifKOjWpLZWlIpOpnmRKPIriAwAbZlFcIDtjYyUNZzsaFOG>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:46.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data4/2gb/VofkqjcbxufnLLqqcWCQhNarmaqaPNTxJzMJjKmavjOMnKovDivdnpQvvPgxDmjfCnacEmtjEGBVpYFLDYEbWNYuqsIQpfMoscKIXiOYtgGdyOTGahtscjZvrCuHBQLy>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:49.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data4/2gb/lVTfSiJrtvOzIyXCowKbiFcJgAqnnrBxuPDTdcMzXItxCvqcylhPZzqHrxHqQdRfCuiYLMqisBrLjfJaraNvhNRHnThcxHHXNVsoOkUXXTthwoeaIKJnDTwOCROgvQEo>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 16:23:47.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 4:41:22.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 4:40:32.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 4:38:10.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 3:48:58.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 3:48:17.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 3:47:48.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 3:40:47.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload largefile/data1/2gb_3/zQRmRMudvDfMWSfXfarPWmFooYwlONPGGvGJjHfJprvHQscfNQCmGlkQgaGHMGYJxbYGPzNXZNiEzajXtnaIOReHOWHlFTStvTjNlKvXNqwFyIHgrsnzTOxWKcbCqVVB>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 12 days, 2:13:31.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload largefile/data1/2gb_4/aaoDGAzAxSiDEzkhaPQSqIbWoCyUvJBGBFHgTqcBaSrboCpuRrWoTTDXcXFAaucVrFDwSKpeWLxZsuQrWYfKiigkpXFQtWZTFDNPUnpWUYojDQtgxwtAEFpxHIiUZhsq>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 10 days, 9:18:38.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload largefile/scratch/jason/bar/en.xml>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
not cleaning, youngest upload part ( 4:03:01.267628 ) was before 7 days, 0:00:00


<MultiPartUpload data1/2gb/IkQMhADWKZJBJVerKeAPwmHumccRYUCGvWnvLCpHOTvtVZuZbsCzjJFEHbwdkcIVjLbqKcrFjzrnXZNiSiJyGGBJfoBiVItfKSXSJdClcFRegitMEgpjeVwbniRWiaRo>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:13:27.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data1/2gb/LOeUprnJxFeHxEXVNedupwjUTVXBMiXnQSaeKYaObsDmBPEvLfyFNlMTtlQrAsTMNDhXBqWzVYjCjvirIiTTVzpFTRDistzJScTpcxJXaZfXcJnMKExbmxnFFayBKMQP>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:56:42.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data1/2gb/gqudcAXxNTXRQdgJVqaKMKMXkqRtWealQIugAJAuGHBOVyBFHudWNxSozDUwtQVpPbHGIyurktCEDmwWiIqSXSxEGnvGyNxxbkziFYJFnqEIpsZlvNKpaEvyvAeARsdl>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:06:12.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data1/2gb/mwoHnLNYkLUlCzbRHVgQaYmVOSUaNNUOuQRRmNYdlATorWWQiWVLzfXcySIDReWxjaBcbVgRgdHUhqdciAcyNjZOKdDWOJLMMdwwUrYPmgnJczJOUbmMbnpmoSwQbxkw>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:06:16.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data1/2gb/uxljMzxfyJqpgDwXxlOvENAfssEtAVlKbzDkrxVXLfsCpdOlRJQjQtpKdMAhngirOXUxkDvDmHpEMIPGikfTgodsiBRqCTqAznIxajuhLMyDACsQSLLzxXLVlMviCtxr>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:56:40.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data2/2gb/ERyNPANEnjXvAYEpVORgVHXCIxvSGFicsCqxTHwflRdHPLXNqYJEIrMXsBohWpKcjFDcWBFYEoiOrAzQuEYshouCgLtaJYsaonvhhYZzHVoCwPXGKGbZZCFgoTPKzgww>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:56:42.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data2/2gb/FRolciVigQXRAXmbxcmZgiKmaMBQAGbICtRZaBafLfQQctRoBLtBlNdJXvaQIQXuZouKZDShvhnBbmUASCIgfhgunKjexIvtrjdfZrYSBWPsciecBbGoCmEwDdiBWpiK>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:06:16.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data2/2gb/FzpxoTnKsRCspOLduRQUDnZQMwCcRaUhZlVXSGsanOZIqSvAntzWqNjaDsZEHMWTOvYIbWHWzozDVQrygoZMfXYihfIppSWyuzwSzSSqnxOdmUEqWDmnftQSiTUnDHKR>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:58:54.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data2/2gb/IHyGUyDlexfFyJCjjdEjmZsbNuEmhSxLBbeaNeUocXwZNQdLelDIWzxVdhcFVmLfCMwHrbSByAgeZEDFhBxZpMZxbsXjvgUdTgiygpbZYhdbZnVOeEpKIoCOBkbFrHkV>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:06:52.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data2/2gb/fsKOgZMjQBQHpnojDUIQIRpvzyAoTpkJbATGbTDjWujpunRCptMAgtbLFdNocyhDKoIkAZCSOKhSkVkSvAdZmblLrMptETZyIEcWsOtweGlSYFbrxGVAjHzbKiDpvyIV>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:51.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data2/2gb/sQRpMgFFxgrLwenpxfjLYsLKDqRubLZkgynglzZxGNHPoTueilJvCIQPUksBYmqkQrXrJFzSMfqkMKAHTPjKlwdVEviSLJWAiTeQOaxkLQEjZAmnJmOLduLjOWsiaFfq>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:12:02.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data3/2gb/DTPMSMcRIzNkWSZsBZaGVUaZowCluWrUycyxagvUEGTmJZnVRIMHoqzyrLXXcabOemXKPvcqKqUNaiAOoayMyNPuEBbDJkZkuAYKQlhZPyATajrRHIjialHmqQwwRuyS>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:57:29.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data3/2gb/QQOgLNTDNtzczUPoeiIztDtytyMnMNWtJOhUxBoSkgfEjbgKVltLKESvNsnWihhlraoguLdezcZNmOjRifAYxCGEmdjWqZhpvUcZElLBoHLUvNfFtItKIrOOueJRJQBp>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:09:59.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data3/2gb/VAUzwAcqtJYBgGhyjeXnyAKOnLXhzHJBZXNIEqtDuLTsMtdBFlQTBknDbWfRdonIzRcWYDVkZHPaJFYYRMxUzDVAwikkQnoWBkJSsaGYiKjyKeKiGRfbACbvQEpnRgTY>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:06:30.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data3/2gb/isdwyOBqnrfjNFejJYWCwBwWctmOBFcvVssYIvJEBRSWmSFBJiiYiWsFTAnXzCUqSnuYnXDmTHDcfPodwXvJvCCWFgXjAEnZoLxBCoZngWRtnqgYsdnzroQkuEeNTlJb>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:52.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data3/2gb/sbAiLNrIjHHFjeqYFfZLPrpGPCnVMZXtfJgtOuzeJdLSyiTxlAtWmQaiJtXIZDTdCryxgjBtsQbwHXQAPAnqPIpaGQKGwcEWgkRJyFioLgroFkDiFcSaKPBrevNHKVQF>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:57:09.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data4/2gb/CBsdQvVAnBGdlaPzeiUWnQRCKBtwgZnJPRkZiZNasFxJlunWuwjmOhXMhZrvjGusiZjVzpoUKBhWPZrfCBhDidBNmLwRsxbkbAVrfPeYklPwwAfaayPUcTDDrVuzjZJn>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:49.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data4/2gb/DzAVuYTTZlWIYSqAGeEanOLfCIAcXuqaueJivawTuzZUpRdLmRIHcXdjmiHIystjzoMVHbyNHgwRrOJffYpOEFCuWVeRfEWELRIULPqRRBGlRgvmJAPGVEuRafvFzeDz>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:49.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data4/2gb/OZbRrpupPsqaLWYvQyLoBMVwDeCkYNNYoreNfnKeskCYCnqEcyKhSovqkukHzyJtjjumgLLoISFVTfJcFCcOizfgsswmceRxEUASDrhxyzNQzCDOFcSyNeUBfKmHcYut>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:05:48.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data4/2gb/ciQtWbkfRzMEbrNqagvzCOcEHJHabQIkFsfnZuBWrsSyyniIHPcBmegHsVQooqEianhhMEDasBBuVCEXZkAuBoxkKEvmagBfMKkTjFiuYtMpdROlVKMvYvZTWbzvajhr>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:56:42.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data4/2gb/qsofBpDgRJCZJakUjXRBGvjULEEraFYsAztCwZmGujzEURwABMTodgkEPtNWixLzScyYOgFLRvpPrPSQeOCTUHJgnJKgVwTQZlhUFxEKZeRuVcZDYbdBrstitayTfAsn>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 10:09:54.267628 ) is more than 7 days, 0:00:00 ago, cleaning


<MultiPartUpload data4/2gb/sRLFVDhuZOLzDXzdQycUewHSQaYZSxEHBCExGLVoItrrLtUcYaTnNMwwqGhYLEyBkWFwgGGevzKznmJudTPAAUDolGIsRwPvJMqxHJsKxYgGgierzqBnVpxXnFfjBJez>
owner name myusername
owner id   000000000000000000000000000000000000000000000000
storage class STANDARD
youngest upload part ( 38 days, 4:56:42.267628 ) is more than 7 days, 0:00:00 ago, cleaning




sum bytes of all uploads 76702547968 ( 71  gb)
sum bytes of uploads older than 7 days, 0:00:00  is  67181477888 ( 62  gb)
```
