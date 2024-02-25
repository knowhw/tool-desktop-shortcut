



##  #Solution
```py
from au.desktop import content
desk = content("geany")


desk.Entry ["Icon"] = "face-heart"
desk.Entry ["Type"] = "Application"
desk.Entry ["Version"] = "1.0"
desk.Entry ["Categories"] = "GTK;Development;IDE;"
desk.Entry ["Name"] = "geany"

test = desk.entry.set(key="Exec", value="/usr/bin/test")

for item in test.print_file():
	print(item)


```



## #Sample Output [/usr/share/applications/myapp.desktop]
```
[Desktop Entry]
Type=Application
Version=1.0
Terminal=false
Categories=GTK;GNOME;Utility;
Icon=face-heart
Name=Geany
Name[zu]=isicelo sami
Name[yo]=mi-elo
Name[yi]=מיין אַפּלאַקיישאַן
Name[xh]=isicelo sam
Name[cy]=fy-cais
Name[vi]=ứng dụng của tôi
Name[uz]=mening ilovam
Name[ug]=مېنىڭ ئىلتىماسىم
Name[ur]=میری درخواست
Name[uk]=моя заявка
Name[ak]=me-application no
Name[tk]=anketam
Name[tr]=benim-uygulamam
Name[ts]=my-xikombelo
Name[ti]=ናተይ-መመልከቲ
Name[th]=ใบสมัครของฉัน
Name[te]=నా దరఖాస్తు
Name[tt]=минем кушымтам
Name[ta]=எனது விண்ணப்பம்
Name[tg]=аризаи ман
Name[sv]=min ansökan
Name[sw]=maombi yangu
Name[su]=abdi-aplikasi
Name[es]=mi aplicación
Name[so]=codsigeyga
Name[sl]=moja-prošnja
Name[sk]=moja aplikácia
Name[si]=මගේ-යෙදුම
Name[sd]=منهنجي درخواست
Name[sn]=yangu-application
Name[st]=tshebediso ya ka
Name[sr]=моја пријава
Name[nso]=my-kgopelo
Name[gd]=m' iarrtas
Name[sa]=मम-अनुप्रयोगः
Name[sm]=la'u talosaga
Name[ru]=мое заявление
Name[ro]=aplicatia mea
Name[qu]=mi-aplicación nisqa
Name[pa]=ਮੇਰੀ-ਐਪਲੀਕੇਸ਼ਨ
Name[pt]=Minha aplicação
Name[pl]=moja aplikacja
Name[fa]=برنامه من
Name[ps]=زما غوښتنلیک
Name[om]=my-iyyata koo
Name[or]=ମୋର ପ୍ରୟୋଗ
Name[no]=min søknad
Name[ne]=मेरो आवेदन
Name[my]=ငါ့လျှောက်လွှာ
Name[mn]=миний програм
Name[lus]=ka-a dilna
Name[mni-Mtei]=ꯑꯩꯒꯤ-ꯑꯦꯞꯂꯤꯀꯦꯁꯟ꯫
Name[mr]=माझा अर्ज
Name[mi]=taku-tono
Name[mt]=l-applikazzjoni tiegħi
Name[ml]=എന്റെ അപേക്ഷ
Name[ms]=permohonan saya
Name[mg]=my-application
Name[mai]=हमर-अनुप्रयोग
Name[mk]=мојата-апликација
Name[lb]=meng Applikatioun
Name[lg]=my-okusaba
Name[lt]=Mano aplikacija
Name[ln]=my-application
Name[lv]=mans pieteikums
Name[la]=mea application
Name[lo]=ຄໍາຮ້ອງສະຫມັກຂອງຂ້ອຍ
Name[ky]=Менин арызым
Name[ckb]=my-application
Name[ku]=min-sepan
Name[kri]=mi-aplikeshɔn
Name[ko]=내 응용 프로그램
Name[gom]=माझें-अर्ज
Name[rw]=Porogaramu
Name[km]=កម្មវិធីរបស់ខ្ញុំ
Name[kk]=менің қолданбам
Name[kn]=ನನ್ನ-ಅರ್ಜಿ
Name[jw]=sandi-aplikasi
Name[ja]=私のアプリケーション
Name[it]=la mia applicazione
Name[ga]=m'iarratas
Name[id]=lamaran saya
Name[ilo]=my-aplikasion
Name[ig]=ngwa m
Name[is]=mitt-umsókn
Name[hu]=az alkalmazásom
Name[hmn]=kuv-application
Name[hi]=मेरा आवेदन
Name[iw]=האפליקציה שלי
Name[haw]=kaʻu-palapala
Name[ha]=aikace-aikace na
Name[ht]=aplikasyon mwen an
Name[gu]=મારી અરજી
Name[gn]=che-aplicación rehegua
Name[el]=η αίτησή μου
Name[de]=meine-Bewerbung
Name[ka]=ჩემი განაცხადი
Name[gl]=a miña aplicación
Name[fy]=myn-applikaasje
Name[fr]=mon application
Name[fi]=minun hakemus
Name[tl]=aking-aplikasyon
Name[ee]=nye-dɔbiagbalẽvi
Name[et]=minu rakendus
Name[eo]=mia-aplikaĵo
Name[en]=my-application
Name[nl]=mijn aanvraag
Name[doi]=मेरा-एप्लीकेशन
Name[dv]=މައި-އެޕްލިކޭޝަން
Name[da]=min-applikation
Name[cs]=moje aplikace
Name[hr]=moja prijava
Name[co]=a mo applicazione
Name[zh-TW]=我的應用程式
Name[zh-CN]=我的应用程序
Name[ny]=ntchito yanga
Name[ceb]=akong-aplikasyon
Name[ca]=la meva-aplicació
Name[bg]=моето приложение
Name[bs]=moja aplikacija
Name[bho]=हमार-आवेदन के बा
Name[bn]=আমার আবেদন
Name[be]=маё-дадатак
Name[eu]=nire-aplikazioa
Name[bm]=my-application (application) ye
Name[az]=mənim tətbiqim
Name[ay]=my-aplicación ukax mä juk’a pachanakanwa
Name[as]=মোৰ-এপ্লিকেচন
Name[hy]=իմ դիմումը
Name[ar]=طلبي
Name[am]=የእኔ-መተግበሪያ
Name[sq]=aplikimi im
Name[af]=my-toepassing
```
