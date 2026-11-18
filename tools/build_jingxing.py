import json, re, sys, collections
D = '/home/claude/jingxing-pin/data/'

INTRO = {
'T0278': [
"爾時，智首菩薩問文殊師利言：「佛子！云何菩薩不染身、口、意業，不害身、口、意業，不癡身、口、意業，不退轉身、口、意業，不動身、口、意業，應讚歎身、口、意業，清淨身、口、意業，離煩惱身、口、意業，隨智慧身、口、意業？云何菩薩生處成就，姓成就，家成就，色相成就，念成就，智慧成就，趣成就，無畏成就，覺悟成就？云何菩薩第一智慧，最上智慧，勝智慧，最勝智慧，不可量智慧，不可數智慧，不可思議智慧，不可稱智慧，不可說智慧？云何菩薩因力具足，意力具足，方便力具足，緣力具足，境界力具足，根力具足，止觀力具足，定力具足？云何菩薩善知陰界入，善知緣起法，善知欲、色、無色界，善知過去、未來、現在？云何菩薩修七覺意，修空、無相、無作？云何菩薩滿足檀波羅蜜、尸波羅蜜、羼提波羅蜜、毘梨耶波羅蜜、禪波羅蜜、般若波羅蜜、慈、悲、喜、捨？云何菩薩得是處、非處智力，過去、未來、現在業報智力，種種諸根智力，種種性智力，種種欲智力，一切至處道智力，禪定解脫三昧垢淨智力，宿命無礙智力，天眼無礙智力，斷一切煩惱習氣智力？云何菩薩常為諸天王守護，恭敬供養；龍王、鬼神王、乾闥婆王、阿脩羅王、迦樓羅王、緊那羅王、摩睺羅伽王、人王、梵天王等守護，恭敬供養？云何菩薩為眾生舍，為救，為歸，為趣，為炬，為明，為燈，為導，為無上導？云何菩薩於一切眾生為第一，為大；為勝；為上；為無上；為無等；為無等等？」",
"爾時，文殊師利答智首菩薩曰：「善哉！善哉！佛子！多所饒益，多所安隱，哀愍世間，惠利一切，安樂天人，問如是義。佛子！菩薩成就身、口、意業，能得一切勝妙功德；於佛正法，心無罣礙；去、來、今佛所轉法輪，能隨順轉；不捨眾生，明達實相；斷一切惡，具足眾善；色像第一，悉如普賢大菩薩等；成就如來一切種智；於一切法悉得自在，而為眾生第二尊導。佛子！何等身、口、意業能得一切勝妙功德？"],
'T0279': [
"爾時，智首菩薩問文殊師利菩薩言：「佛子！菩薩云何得無過失身、語、意業？云何得不害身、語、意業？云何得不可毀身、語、意業？云何得不可壞身、語、意業？云何得不退轉身、語、意業？云何得不可動身、語、意業？云何得殊勝身、語、意業？云何得清淨身、語、意業？云何得無染身、語、意業？云何得智為先導身、語、意業？云何得生處具足、種族具足、家具足、色具足、相具足、念具足、慧具足、行具足、無畏具足、覺悟具足？云何得勝慧、第一慧、最上慧、最勝慧、無量慧、無數慧、不思議慧、無與等慧、不可量慧、不可說慧？云何得因力、欲力、方便力、緣力、所緣力、根力、觀察力、奢摩他力、毘鉢舍那力、思惟力？云何得蘊善巧、界善巧、處善巧、緣起善巧、欲界善巧、色界善巧、無色界善巧、過去善巧、未來善巧、現在善巧？云何善修習念覺分、擇法覺分、精進覺分、喜覺分、猗覺分、定覺分、捨覺分、空、無相、無願？云何得圓滿檀波羅蜜、尸波羅蜜、羼提波羅蜜、毘梨耶波羅蜜、禪那波羅蜜、般若波羅蜜，及以圓滿慈、悲、喜、捨？云何得處非處智力、過未現在業報智力、根勝劣智力、種種界智力、種種解智力、一切至處道智力、禪解脫三昧染淨智力、宿住念智力、無障礙天眼智力、斷諸習智力？云何常得天王、龍王、夜叉王、乾闥婆王、阿脩羅王、迦樓羅王、緊那羅王、摩睺羅伽王、人王、梵王之所守護，恭敬供養？云何得與一切眾生為依、為救、為歸、為趣、為炬、為明、為照、為導、為勝導、為普導？云何於一切眾生中，為第一、為大、為勝、為最勝、為妙、為極妙、為上、為無上、為無等、為無等等？」",
"爾時，文殊師利菩薩告智首菩薩言：「善哉！佛子！汝今為欲多所饒益、多所安隱，哀愍世間，利樂天人，問如是義。佛子！若諸菩薩善用其心，則獲一切勝妙功德；於諸佛法，心無所礙，住去、來、今諸佛之道；隨眾生住，恒不捨離；如諸法相，悉能通達；斷一切惡，具足眾善；當如普賢，色像第一，一切行願皆得具足；於一切法，無不自在，而為眾生第二導師。佛子！云何用心能獲一切勝妙功德？佛子！"]}
OUTRO = {
'T0278': ["「佛子！是為菩薩身、口、意業能得一切勝妙功德，諸天、魔、梵、沙門、婆羅門、人及非人、聲聞、緣覺所不能動。」"],
'T0279': ["「佛子！若諸菩薩如是用心，則獲一切勝妙功德；一切世間諸天、魔、梵、沙門、婆羅門、乾闥婆、阿脩羅等，及以一切聲聞、緣覺，所不能動。」"]}

NOTES = {
'T0278': [
('0430c05','戀','戀【大】，變【聖】'),('0430c10','離','離【大】，去【宋】【元】【明】【宮】【聖】'),
('0430c15','處','處【大】，會【宋】【元】【明】【宮】'),('0430c20','深入','深入【大】，入深【宋】【元】【明】【宮】【聖】'),
('0430c23','除鬀','除鬀【大】，除剃【宋】【元】【明】，除剔【宮】，剃除【聖】'),('0431a05','尚','尚【大】，上【聖】'),
('0431a11','跏','跏【大】＊，加【宮】＊'),('0431a15','跏','跏【大】＊，加【宮】＊（同前，＊）'),
('0431b10','行','行【大】，求【宋】【元】【明】'),('0431b20','阬','阬【大】，坑【宋】【元】【明】【宮】【聖】'),
('0431b21','訟','訟【大】，誦【宋】【元】【明】'),('0431c06','海智','海智【大】，智海【聖】'),('0431c06','智','智【大】，音【宋】【元】【明】【宮】'),
('0431c07','辯','辯【大】＊，辨【聖】＊'),('0431c13','𦓷','𦓷【大】，芸【宋】【元】【明】【宮】【聖】'),
('0431c22','憺怕','憺怕【大】，淡泊【宮】【聖】'),('0431c25','耄','耄【大】，耘【宋】【元】【明】，秏【宮】'),
('0432a12','辯','辯【大】＊（同前，＊，聖本作辨，依前條）'),
('0432a14','得','得【大】，淨【宋】【元】【明】【宮】【聖】'),('0432a20','沮','沮【大】，俎【聖】'),
('0432b12','意','意【大】，恚【明】'),('0432b14','嚥','嚥【大】，咽【宋】【元】【明】【宮】【聖】'),
('0432c01','塔','塔【大】，境【聖】'),('0432c03','重','重【大】，貴【宮】【聖】'),('0432c08','詠','詠【大】，咏【聖】'),
('0432c14','智','智【大】，知【宋】【元】【明】【宮】')],
'T0279': [
('0070a07','怨','怨【大】，冤【明】'),('0070a09','妓','妓【大】＊，伎【宮】＊'),('0070a10','妓','妓【大】＊（同前，＊）'),
('0070b07','和尚','和尚【大】，和上【宮】'),('0070b13','結跏','結跏【大】，結加【宮】'),
('0070b21','帬','帬【大】，裙【宋】【元】【明】【宮】【聖?—僅列宋元明宮】'),
('0072a14','具神足力','具神足力【大】，具足神力【宋】')]}
# fix typo-prone note: keep exactly as CBETA
NOTES['T0279'][5] = ('0070b21','帬','帬【大】，裙【宋】【元】【明】【宮】')

ANCH = {
'T0278': [('在家','菩薩在家'),('捨家','以信捨家'),('剃度','脫去俗服'),('皈戒','自歸於佛'),('禪堂','若入房舍'),('威儀','下床安足'),('行腳','手執錫杖'),('乞食','入里乞食'),('說法禮佛','若說法時'),('寢息','若洗足時')],
'T0279': [('在家','菩薩在家'),('捨家','捨居家時'),('剃度','脫去俗服'),('皈戒','自歸於佛'),('禪堂','若入堂宇'),('威儀','下足住時'),('行腳','手執錫杖'),('乞食','入里乞食'),('說法禮佛','若說法時'),('寢息','若洗足時')]}
SRC = {'T0278':('CBETA T0278 卷6 〈淨行品第七〉（六十華嚴，東晉佛馱跋陀羅譯，T09n0278_p0430a22–p0432c17；大正藏底本）','T09n0278'),
       'T0279':('CBETA T0279 卷14 〈淨行品第十一〉（八十華嚴，唐實叉難陀譯，T10n0279_p0069b19–p0072a21；大正藏底本）','T10n0279')}
FN = {'T0278':'t0278_lines.txt','T0279':'t0279_lines.txt'}
OUT = {'T0278':'t0278_jingxing.json','T0279':'t0279_jingxing.json'}

def load(w):
    lines=[]
    for ln in open(D+'src/'+FN[w],encoding='utf-8'):
        ln=ln.rstrip('\n')
        if not ln: continue
        k,t=ln.split('\t'); lines.append((k,t))
    return lines

def check_seq(lines):
    gaps=[]
    prev=None
    for k,_ in lines:
        pg=k[:4]; col=k[4]; n=int(k[5:])
        if prev:
            ppg,pcol,pn=prev
            ok = (pg==ppg and col==pcol and n==pn+1) or (pg==ppg and col!=pcol and n==1 and ord(col)==ord(pcol)+1) or (pg!=ppg and col=='a' and n==1 and int(pg)==int(ppg)+1)
            if not ok: gaps.append((ppg+pcol+'%02d'%pn,k))
        prev=(pg,col,n)
    return gaps

res={}
for w in ('T0278','T0279'):
    lines=load(w)
    gaps=check_seq(lines)
    full=''; offs=[]
    for k,t in lines:
        offs.append((len(full),k)); full+=t
    # split at 。
    verses=[]; pos=0
    for m in re.finditer('。',full):
        verses.append((pos,m.end())); pos=m.end()
    tail=full[pos:]
    def line_of(off):
        r=None
        for o,k in offs:
            if o<=off: r=k
            else: break
        return r
    V=[]
    for i,(a,b) in enumerate(verses,1):
        txt=full[a:b]
        V.append({'n':i,'text':txt.lstrip('「'),'line':line_of(a),'_a':a,'_b':b})
    # clause parse
    for v in V:
        parts=re.split('[，：]',v['text'].rstrip('。'))
        v['_parts']=parts
        v['cond']=parts[0]
        v['has_vow']='當願眾生' in v['text']
    # notes
    linestart={k:o for o,k in offs}; linetext=dict(lines)
    for (lk,base,note) in NOTES[w]:
        off=linestart[lk]+linetext[lk].index(base)
        for v in V:
            if v['_a']<=off<v['_b']:
                v.setdefault('notes',[]).append(note)
    # sections
    anc=ANCH[w]; idx=[]
    for name,cond in anc:
        hit=[v['n'] for v in V if v['cond']==cond]
        idx.append((name,hit))
    ranges=[]
    for j,(name,hit) in enumerate(idx):
        if len(hit)!=1: ranges.append((name,None,None,'待核:起點「%s」命中%d處'%(anc[j][1],len(hit)))); continue
        start=hit[0]
        end=None
        if j+1<len(idx) and len(idx[j+1][1])==1: end=idx[j+1][1][0]-1
        elif j+1==len(idx): end=len(V)
        ranges.append((name,start,end,''))
    for v in V:
        v['section']='待核'
        for name,s,e,_ in ranges:
            if s and e and s<=v['n']<=e: v['section']=name
        parts=v['_parts']
        if v['has_vow'] and len(parts)==4:
            v['vow']='，'.join(parts[2:])+'。'
        else: v['vow']=None
    cnt_verses=sum(1 for v in V if v['has_vow'])
    cnt_occ=full.count('當願眾生')
    cnt_start=sum(1 for v in V if v['text'].startswith('當願眾生'))
    not4=[v['n'] for v in V if len(v['_parts'])!=4]
    ln_start,ln_end=lines[0][0],lines[-1][0]
    doc={'source':SRC[w][0],'work':w,'verse_line_range':f'{SRC[w][1]}_p{ln_start}–p{ln_end}',
         'note':'逐字取自 CBETA（cbdata.dila.edu.tw /stable/lines）大正藏底本，未改字；異體字（如 𦓷、憺怕、鬀、麁歰/麁澁、帬、阬）照 CBETA 原樣。第1偈原文開頭有引號「，已移到 intro/不在 text。section 為依偈文內容初擬之十篇歸屬，未見規劃定稿原文，尚待核；身/語/意歸屬 CBETA 原文未標，不另標（待核）。',
         'count_vow_verses':cnt_verses,'count_total_units':len(V),
         'intro':INTRO[w],'verses':[{k:v[k] for k in ('n','text','line','section','cond','vow') }|({'notes':v['notes']} if 'notes' in v else {}) for v in V],
         'outro':OUTRO[w],
         'ranges':[{'section':n,'from':s,'to':e,'check':c} for n,s,e,c in ranges],
         'intro_notes_status':'待核：intro/outro 的 CBETA 校勘註（如 色/止/尸/禪 等）未逐條擷取'}
    json.dump(doc,open(D+OUT[w],'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    res[w]=dict(gaps=gaps,tail=tail,verses=V,cnt_verses=cnt_verses,cnt_occ=cnt_occ,cnt_start=cnt_start,not4=not4,ranges=ranges,total=len(V))
    print(w,'lines',len(lines),'gaps',gaps,'tail',repr(tail),'units',len(V),'vow verses',cnt_verses,'occ',cnt_occ,'start-with',cnt_start,'not4',not4)
    print(ranges)
json.dump({w:{k:v for k,v in r.items() if k!='verses'} for w,r in res.items()},open('/tmp/res.json','w'),ensure_ascii=False)
import pickle; pickle.dump(res,open('/tmp/res.pkl','wb'))
