class script(object):
    START_TXT = """<b>๐ฏ๐๐{},
๐ผ๐๐ ๐๐ ๐๐ค ๐๐ค๐ช๐ง ๐๐ง๐ค๐ช๐ฅ..
โ๏ธ ๐๐๐ ๐ ๐๐ ๐ผ๐จ ๐ผ๐๐ข๐๐ฃ...
โ๏ธ ๐ ๐๐๐๐ ๐๐ง๐ค๐ซ๐๐๐ ๐๐๐๐๐๐ ๐๐๐๐ง๐ ๐ฌ
โ๏ธ ๐๐ค ๐พ๐ค๐ฅ๐ฎ๐ง๐๐๐๐ฉ ๐๐จ๐จ๐ช๐ ๐๐ฃ ๐๐ค๐ช๐ง ๐๐ง๐ค๐ช๐ฅ ๐ฅฐ..,
โ๏ธ ๐๐๐๐ฃ ๐๐๐ ๐๐ฎ ๐๐ค๐ฌ๐๐ง๐จ ๐๐ฃ ๐๐ค๐ช๐ง ๐๐ง๐ค๐ช๐ฅ ๐ฅ</b>"""
    HELP_TXT = """<b>Hแดส {}
Hแดสแด Is Tสแด Hแดสแด Fแดส Mส Cแดแดแดแดษดแดs.</b>"""
    ABOUT_TXT = """<b>โช ๐ด๐ ๐๐๐๐ : {}
โช ๐ช๐๐๐๐๐๐ : <a href='https://t.me/MB_Owner'>สแดสแดแด๊ฑแดแดส</a>
โช ๐ซ๐๐๐๐๐๐๐๐ : <a href='https://t.me/AFxSU'>ษำผ_ีผรถึ</a>
โช ๐ณ๐๐๐๐๐๐ : ๐ท๐๐๐๐๐๐๐
โช ๐ณ๐๐๐๐๐๐๐ : ๐ท๐๐๐๐๐ 3
โช ๐ซ๐๐๐ ๐๐๐๐ : ๐ด๐๐๐๐๐ซ๐ฉ
โช ๐ฉ๐๐ ๐๐๐๐๐๐ : ๐ฏ๐๐๐๐๐
โช ๐ฉ๐๐๐๐ ๐บ๐๐๐๐๐ : v2.0.3 [ ๐บ๐๐๐๐๐ ]</b>"""
    SOURCE_TXT = """<b>ษดแดแดแด:
- แดสษช๊ฑ สแดแด ษช๊ฑ แดษด แดแดแดษด ๊ฑแดแดสแดแด แดสแดแดแดแดแด.
- ๊ฑแดแดสแดแด - <a href="https://t.me/AdhavaaBiriyaniKittiyalo">สแดสแด</a>
</b>"""
    MANUELFILTER_TXT = """สแดสแด: <b>๊ฐษชสแดแดส๊ฑ</b>
- ๊ฐษชสแดแดส ษช๊ฑ แด ๊ฐแดแดแดแดสแด แดกแดสแด แด๊ฑแดส๊ฑ แดแดษด ๊ฑแดแด แดแดแดแดแดแดแดแดแด สแดแดสษชแด๊ฑ ๊ฐแดส แด แดแดสแดษชแดแดสแดส แดแดสแดกแดสแด แดษดแด ษช แดกษชสส สแด๊ฑแดแดษดแด แดกสแดษดแดแด แดส แด แดแดสแดกแดสแด ษช๊ฑ ๊ฐแดแดษดแด ษชษด แดสแด แดแด๊ฑ๊ฑแดษขแด
<b>ษดแดแดแด:</b>
1. แดสษช๊ฑ สแดแด ๊ฑสแดแดสแด สแดแด แด แดแดแดษชษด แดสษชแด ษชสแดษขแด.
2. แดษดสส แดแดแดษชษด๊ฑ แดแดษด แดแดแด ๊ฐษชสแดแดส๊ฑ ษชษด แด แดสแดแด.
3. แดสแดสแด สแดแดแดแดษด๊ฑ สแดแด แด แด สษชแดษชแด แด๊ฐ 64 แดสแดสแดแดแดแดส๊ฑ.
Cแดแดแดแดษดแดs Aษดแด Usแดษขแด:
โข /filter - <code>แดแดแด แด ๊ฐษชสแดแดส ษชษด แด แดสแดแด</code>
โข /filters - <code>สษช๊ฑแด แดสส แดสแด ๊ฐษชสแดแดส๊ฑ แด๊ฐ แด แดสแดแด</code>
โข /del - <code>แดแดสแดแดแด แด ๊ฑแดแดแดษช๊ฐษชแด ๊ฐษชสแดแดส ษชษด แด แดสแดแด</code>
โข /delall - <code>แดแดสแดแดแด แดสแด แดกสแดสแด ๊ฐษชสแดแดส๊ฑ ษชษด แด แดสแดแด (แดสแดแด แดแดกษดแดส แดษดสส)</code>"""
    BUTTON_TXT = """สแดสแด: <b>สแดแดแดแดษด๊ฑ</b>
- แดสษช๊ฑ สแดแด ๊ฑแดแดแดแดสแด๊ฑ สแดแดส แดสส แดษดแด แดสแดสแด ษชษดสษชษดแด สแดแดแดแดษด๊ฑ.
<b>ษดแดแดแด:</b>
1. แดแดสแดษขสแดแด แดกษชสส ษดแดแด แดสสแดแดก๊ฑ สแดแด แดแด ๊ฑแดษดแด สแดแดแดแดษด๊ฑ แดกษชแดสแดแดแด แดษดส แดแดษดแดแดษดแด, ๊ฑแด แดแดษดแดแดษดแด ษช๊ฑ แดแดษดแดแดแดแดสส.
2. แดสษช๊ฑ สแดแด ๊ฑแดแดแดแดสแด๊ฑ สแดแดแดแดษด๊ฑ แดกษชแดส แดษดส แดแดสแดษขสแดแด แดแดแดษชแด แดสแดแด.
3. สแดแดแดแดษด๊ฑ ๊ฑสแดแดสแด สแด แดสแดแดแดสสส แดแดส๊ฑแดแด แด๊ฑ แดแดสแดแดแดแดกษด ๊ฐแดสแดแดแด
<b>แดสส สแดแดแดแดษด๊ฑ:</b>
<code>[Button Text](buttonurl:https://t.me/jd_The_File_Donor_Updates)</code>
<b>แดสแดสแด สแดแดแดแดษด๊ฑ:</b>
<code>[Button Text](buttonalert:แดสษช๊ฑ ษช๊ฑ แดษด แดสแดสแด แดแด๊ฑ๊ฑแดษขแด)</code>"""
    AUTOFILTER_TXT = """สแดสแด: <b>แดแดแดแด ๊ฐษชสแดแดส</b>
<b>ษดแดแดแด: Fษชสแด Iษดแดแดx</b>
1. แดแดแดแด แดแด แดสแด แดแดแดษชษด แด๊ฐ สแดแดส แดสแดษดษดแดส ษช๊ฐ ษชแด'๊ฑ แดสษชแด แดแดแด.
2. แดแดแดแด ๊ฑแดสแด แดสแดแด สแดแดส แดสแดษดษดแดส แดแดแด๊ฑ ษดแดแด แดแดษดแดแดษชษด๊ฑ แดแดแดสษชแด๊ฑ, แดแดสษด แดษดแด ๊ฐแดแดแด ๊ฐษชสแด๊ฑ.
3. ๊ฐแดสแดกแดสแด แดสแด สแด๊ฑแด แดแด๊ฑ๊ฑแดษขแด แดแด แดแด แดกษชแดส Qแดแดแดแด๊ฑ. ษช'สส แดแดแด แดสส แดสแด ๊ฐษชสแด๊ฑ ษชษด แดสแดแด แดสแดษดษดแดส แดแด แดส แดส.

<b>Nแดแดแด: AแดแดแดFษชสแดแดส</b>
1. Aแดแด แดสแด สแดแด แดs แดแดแดษชษด แดษด สแดแดส ษขสแดแดแด.
2. Usแด /connect แดษดแด แดแดษดษดแดแดแด สแดแดส ษขสแดแดแด แดแด แดสแด สแดแด.
3. Usแด /settings แดษด สแดแด's PM แดษดแด แดแดสษด แดษด AแดแดแดFษชสแดแดส แดษด แดสแด sแดแดแดษชษดษขs แดแดษดแด."""
    CONNECTION_TXT = """สแดสแด: <b>แดแดษดษดแดแดแดษชแดษด๊ฑ</b>
- แด๊ฑแดแด แดแด แดแดษดษดแดแดแด สแดแด แดแด แดแด ๊ฐแดส แดแดษดแดษขษชษดษข ๊ฐษชสแดแดส๊ฑ 
- ษชแด สแดสแด๊ฑ แดแด แดแด แดษชแด ๊ฑแดแดแดแดษชษดษข ษชษด ษขสแดแดแด๊ฑ.
<b>ษดแดแดแด:</b>
1. แดษดสส แดแดแดษชษด๊ฑ แดแดษด แดแดแด แด แดแดษดษดแดแดแดษชแดษด.
2. ๊ฑแดษดแด <code>/แดแดษดษดแดแดแด</code> ๊ฐแดส แดแดษดษดแดแดแดษชษดษข แดแด แดแด สแดแดส แดแด
Cแดแดแดแดษดแดs Aษดแด Usแดษขแด:
โข /connect  - <code>แดแดษดษดแดแดแด แด แดแดสแดษชแดแดสแดส แดสแดแด แดแด สแดแดส แดแด</code>
โข /disconnect  - <code>แดษช๊ฑแดแดษดษดแดแดแด ๊ฐสแดแด แด แดสแดแด</code>
โข /connections - <code>สษช๊ฑแด แดสส สแดแดส แดแดษดษดแดแดแดษชแดษด๊ฑ</code>"""
    EXTRAMOD_TXT = """สแดสแด: Exแดสแด Mแดแดแดสแดs
<b>ษดแดแดแด:</b>
แดสแด๊ฑแด แดสแด แดสแด แดxแดสแด ๊ฐแดแดแดแดสแด๊ฑ แด๊ฐ แดสษช๊ฑ สแดแด
Cแดแดแดแดษดแดs Aษดแด Usแดษขแด:
โข /id - <code>ษขแดแด ษชแด แด๊ฐ แด ๊ฑแดแดแดษช๊ฐษชแดแด แด๊ฑแดส.</code>
โข /info  - <code>ษขแดแด ษชษด๊ฐแดสแดแดแดษชแดษด แดสแดแดแด แด แด๊ฑแดส.</code>
โข /imdb  - <code>ษขแดแด แดสแด ๊ฐษชสแด ษชษด๊ฐแดสแดแดแดษชแดษด ๊ฐสแดแด ษชแดแดส ๊ฑแดแดสแดแด.</code>
โข /search  - <code>ษขแดแด แดสแด ๊ฐษชสแด ษชษด๊ฐแดสแดแดแดษชแดษด ๊ฐสแดแด แด แดสษชแดแด๊ฑ ๊ฑแดแดสแดแด๊ฑ.</code>"""
    ADMIN_TXT = """สแดสแด: Aแดแดษชษด Mแดแดs
<b>ษดแดแดแด:</b>
Tสษชs Mแดแดแดสแด Oษดสส Wแดสแดs Fแดส Mส Aแดแดษชษดs
Cแดแดแดแดษดแดs Aษดแด Usแดษขแด:
โข /logs - <code>แดแด ษขแดแด แดสแด สแดแดแดษดแด แดสสแดส๊ฑ</code>
โข /stats - <code>แดแด ษขแดแด ๊ฑแดแดแดแด๊ฑ แด๊ฐ ๊ฐษชสแด๊ฑ ษชษด แดส. [Tสษชs Cแดแดแดแดษดแด Cแดษด Bแด Usแดแด Bส Aษดสแดษดแด]</code>
โข /delete - <code>แดแด แดแดสแดแดแด แด ๊ฑแดแดแดษช๊ฐษชแด ๊ฐษชสแด ๊ฐสแดแด แดส.</code>
โข /users - <code>แดแด ษขแดแด สษช๊ฑแด แด๊ฐ แดส แด๊ฑแดส๊ฑ แดษดแด ษชแด๊ฑ.</code>
โข /chats - <code>แดแด ษขแดแด สษช๊ฑแด แด๊ฐ แดส แดสแดแด๊ฑ แดษดแด ษชแด๊ฑ</code>
โข /leave  - <code>แดแด สแดแดแด แด ๊ฐสแดแด แด แดสแดแด.</code>
โข /disable  -  <code>แดแด แดษช๊ฑแดสสแด แด แดสแดแด.</code>
โข /ban  - <code>แดแด สแดษด แด แด๊ฑแดส.</code>
โข /unban  - <code>แดแด แดษดสแดษด แด แด๊ฑแดส.</code>
โข /channel - <code>แดแด ษขแดแด สษช๊ฑแด แด๊ฐ แดแดแดแดส แดแดษดษดแดแดแดแดแด แดสแดษดษดแดส๊ฑ</code>
โข /broadcast - <code>แดแด สสแดแดแดแดแด๊ฑแด แด แดแด๊ฑ๊ฑแดษขแด แดแด แดสส แด๊ฑแดส๊ฑ</code>
โข /grp_broadcast - <code>Tแด สสแดแดแดแดแดsแด แด แดแดssแดษขแด แดแด แดสส แดแดษดษดแดแดแดแดแด ษขสแดแดแดs.</code>
โข /gfilter - <code>แดแด แดแดแด ษขสแดสแดส าษชสแดแดสs</code>
โข /gfilters - <code>แดแด แด ษชแดแดก สษชsแด แดา แดสส ษขสแดสแดส าษชสแดแดสs</code>
โข /delg - <code>แดแด แดแดสแดแดแด แด sแดแดแดษชาษชแด ษขสแดสแดส าษชสแดแดส</code>
โข /status - <code>แดแด ษขแดแด sแดแดแดแดs แดา sแดสแด แดส [Tสษชs Cแดแดแดแดษดแด Cแดษด Bแด Usแดแด Bส Aษดสแดษดแด]</code>"""
    STATUS_TXT = """<b>โช Tแดแดแดส Fษชสแดs: <code>{}</code>
โช Tแดแดแดส Usแดสs: <code>{}</code>
โช Tแดแดแดส Cสแดแดs: <code>{}</code>
โช Usแดแด Sแดแดสแดษขแด: <code>{}</code>
โช Fสแดแด Sแดแดสแดษขแด: <code>{}</code></b>"""
    LOG_TEXT_G = """#NewGroup
โชGสแดแดแด = {}(<code>{}</code>)

โชTแดแดแดส Mแดแดสแดสs = <code>{}</code>

โชAแดแดแดแด Bส - {}
"""
    LOG_TEXT_P = """#NewUser
โชID - <code>{}</code>
โชNแดแดแด - {}
"""
    ALRT_TXT = """สแดสสแด {},
แดสษช๊ฑ ษช๊ฑ ษดแดแด สแดแดส แดแดแด ษชแด สแดQแดแด๊ฑแด,
สแดQแดแด๊ฑแด สแดแดส'๊ฑ...
"""

    OLD_ALRT_TXT = """สแดส {},
สแดแด แดสแด แด๊ฑษชษดษข แดษดแด แด๊ฐ แดส แดสแด แดแด๊ฑ๊ฑแดษขแด๊ฑ, 
แดสแดแด๊ฑแด ๊ฑแดษดแด แดสแด สแดQแดแด๊ฑแด แดษขแดษชษด.
"""

    CUDNT_FND = """ษช แดแดแดสแดษด'แด ๊ฐษชษดแด แดษดสแดสษชษดษข สแดสแดแดแดแด แดแด {}
แดษชแด สแดแด แดแดแดษด แดษดส แดษดแด แด๊ฐ แดสแด๊ฑแด?
"""

    I_CUDNT = """ษช แดแดแดสแดษด'แด ๊ฐษชษดแด แดษดส แดแดแด ษชแด สแดสแดแดแดแด แดแด {}
"""

    I_CUD_NT = """ษช แดแดแดสแดษด'แด ๊ฐษชษดแด แดษดส แดแดแด ษชแด สแดสแดแดแดแด แดแด {}.
แดสแดแด๊ฑแด แดสแดแดแด แดสแด ๊ฑแดแดสสษชษดษข แดษด ษขแดแดษขสแด แดส ษชแดแดส...
"""

    MVE_NT_FND = """แดแดแด ษชแด ษดแดแด ๊ฐแดแดษดแด ษชษด แดแดแดแดสแด๊ฑแด...
"""

    TOP_ALRT_MSG = """Cสแดแดแดษชษดษข Fแดส Mแดแด ษชแด Iษด Dแดแดแดสแดsแด...
"""

    MELCOW_ENG = """<b>๐ฏ๐๐๐๐ {}, 
Wแดสแดแดแดแด แดแดส Gสแดแดแด โค๏ธโ๐ฅ
โ Tสษชs ษชs แด แดแดแด ษชแด ษขสแดแดแด
โ Aสส แดแดแดแดษขแดสษชแดs แดา แดแดแด ษชแดs แดแด แดษชสแดสสแด สแดสแด.
โ Jแดsแด แดสแดแด แดสแด แดแดแด ษชแด ษดแดแดแด
โ Oแดส ๐ฑ๐ซ (bot) แดกษชสส sแดษดแด สแดแด แดแดแด ษชแด.
โ ๏ธ ๐ณ๐๐ด ๐๐พ ๐ฒ๐พ๐ฟ๐๐๐ธ๐ถ๐ท๐ ๐ธ๐๐๐๐ด ๐ฐ๐ป๐ป ๐๐ท๐ด ๐ฒ๐ท๐ฐ๐๐ & ๐ต๐ธ๐ป๐๐ด๐๐ ๐๐ธ๐ป๐ป ๐ฑ๐ด ๐ณ๐ด๐ป๐ด๐๐ด๐ณ ๐ธ๐ฝ 10 ๐ผ๐ธ๐ฝโฑ๏ธ.
Iา แดษดส แดแดแดสแด สแดแด แดแดษด สแดแดแด สแดสแดs.
Tสแดษดแด สแดแด ๐ฅฐ</b>
"""

    OWNER_INFO = """
<b>โโโโ[ แดแดแดแดษชส๊ฑ ]โโโโ
โช ๐ซ๐๐๐๐๐๐๐๐ :  
- <a href='t.me/AFxSU'>ษำผ_ีผรถึ</a>
โช ๐ช๐๐๐๐๐๐ :
- <a href='t.me/MB_Owner'>สแดส แดแด๊ฑแดแดส
</a>
"""

    REQINFO = """
โ  ษชษด๊ฐแดสแดแดแดษชแดษด โ 

แด๊ฐแดแดส 10 แดษชษดแดแดแด๊ฑ แดสษช๊ฑ แดแด๊ฑ๊ฑแดษขแด แดกษชสส สแด แดแดแดแดแดแดแดษชแดแดสสส แดแดสแดแดแดแด

ษช๊ฐ สแดแด แดแด ษดแดแด ๊ฑแดแด แดสแด สแดวซแดแดsแดแดแด แดแดแด ษชแด / sแดสษชแดs ๊ฐษชสแด, สแดแดแด แดแด แดสแด ษดแดxแด แดแดษขแด
"""

    MINFO = """
โฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏ
แดแดแด ษชแด สแดวซแดแด๊ฑแด ๊ฐแดสแดแดแด
โฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏ

ษขแด แดแด ษขแดแดษขสแด โ  แดสแดแด แดแดแด ษชแด ษดแดแดแด โ  แดแดแดส แดแดสสแดแดแด ษดแดแดแด โ  แดแด๊ฑแดแด แดสษช๊ฑ ษขสแดแดแด

แดxแดแดแดสแด : Uncharted

๐ฏ แดแดษดแด แด๊ฑแด โ  ':(!,./)
"""

    SINFO = """
โฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏ
๊ฑแดสษชแด๊ฑ สแดวซแดแด๊ฑแด ๊ฐแดสแดแดแด
โฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏโฏ

ษขแด แดแด ษขแดแดษขสแด โ  แดสแดแด ๊ฑแดสษชแด๊ฑ ษดแดแดแด โ  แดแดแดส แดแดสสแดแดแด ษดแดแดแด โ  แดแด๊ฑแดแด แดสษช๊ฑ ษขสแดแดแด

แดxแดแดแดสแด : Loki S01E01

๐ฏ แดแดษดแด แด๊ฑแด โ  ':(!,./)
"""

    NORSLTS = """
โ #๐ก๐ผ๐ฅ๐ฒ๐๐๐น๐๐ โ

๐๐ <b>: {}</b>

๐ก๐ฎ๐บ๐ฒ <b>: {}</b>

๐ ๐ฒ๐๐๐ฎ๐ด๐ฒ <b>: {}</b>
"""

    CAPTION = """
<b>๐ Fษชสแด ษดแดแดแด : </b> <code>{file_name}</code>

<b>
โญโโโโโโโ โข โ โข โโโโโโโโฎ
๐ Dแดสแด Mแดแดแด :  <a href="https://t.me/addtheme/DQ_The_File_Donor_Theme">Tแดแดแดส</a>
โฐโโโโโโโ โข โ โข โโโโโโโโฏ

=========== โข โ  โข ===========
โซ๏ธ sแดแดแดแดสแด ษขสแดแดแด : @bots_supported
=========== โข โ  โข ===========</b>"""
