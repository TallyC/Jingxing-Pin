import json
D='/home/claude/jingxing-pin/data/'
a=json.load(open(D+'t0278_jingxing.json',encoding='utf-8')); b=json.load(open(D+'t0279_jingxing.json',encoding='utf-8'))
def get(doc,cond):
    return [v for v in doc['verses'] if v['cond']==cond]
def fmt(doc,cond):
    r=get(doc,cond)
    if not r: return '（無此偈，起句「%s」查無）'%cond
    return '；'.join('#%d [%s] %s'%(v['n'],v['line'],v['text']) for v in r)
items=[
('出家一願：如佛出家／同佛出家','受出家法','正出家時'),
('求出家法','求出家法','求請出家'),
('受著袈裟／著袈裟衣','受著袈裟','著袈裟衣'),
('飯食已訖','飯食已訖','飯食已訖'),
('晨朝覺悟／睡眠始寤','晨朝覺悟','睡眠始寤'),
('若見空鉢','若見空鉢','若見空鉢'),
('若見滿鉢','若見滿鉢','若見滿鉢'),
('寢息：昏夜寢息／以時寢息','昏夜寢息','以時寢息'),
('除鬀鬚髮／鬀除鬚髮','除鬀鬚髮','鬀除鬚髮'),
('始請和尚／受和尚教','始請和尚','受和尚教'),
('若得食時 vs 若得恭敬','若得食時','若得恭敬'),
('若不得食 vs 不得恭敬','若不得食','不得恭敬'),
('得香美食 vs 若得美食','得香美食','若得美食'),
('若嚥食時 vs 若飯食時','若嚥食時','若飯食時'),
('所食雜味 vs 若受味時','所食雜味','若受味時'),
('退坐出堂 vs 從舍出時','退坐出堂','從舍出時'),
]
ca=[v['cond'] for v in a['verses']]; cb=[v['cond'] for v in b['verses']]
only_a=[c for c in ca if c not in cb]; only_b=[c for c in cb if c not in ca]
L=[]
L.append('# 淨行品兩版 CBETA 逐字資料：檢查報告\n')
L.append('資料日期：2026-11-18。來源：CBETA（cbdata.dila.edu.tw /stable/lines 逐行取得；cbetaonline 頁面對照），底本為大正藏。\n')
L.append('## 一、檔案\n')
L.append('- /home/claude/jingxing-pin/data/t0278_jingxing.json（六十華嚴 T09n0278 卷6〈淨行品第七〉）\n- /home/claude/jingxing-pin/data/t0279_jingxing.json（八十華嚴 T10n0279 卷14〈淨行品第十一〉）\n- /home/claude/jingxing-pin/data/src/*.txt（逐行原文，含 CBETA 行號）；建置腳本在 /home/claude/jingxing-pin/tools/\n')
L.append('## 二、願數（機器計數）\n')
L.append('| 版本 | 以「。」切出的偈數 | 含「當願眾生」的偈數 | 「當願眾生」出現次數 | CBETA 全文檢索「當願眾生」命中（本卷） |\n|---|---|---|---|---|')
L.append('| 六十華嚴 T0278 卷6 | %d | %d | %d | 140 |'%(a['count_total_units'],a['count_vow_verses'],sum(v['text'].count('當願眾生') for v in a['verses']))) 
L.append('| 八十華嚴 T0279 卷14 | %d | %d | %d | 141 |\n'%(b['count_total_units'],b['count_vow_verses'],sum(v['text'].count('當願眾生') for v in b['verses'])))
L.append('- 八十華嚴 141，與聖嚴法師所說 141 願相符；六十華嚴本卷為 140，比 141 少 1 偈。\n- 說明：偈數＝每條「某事，當願眾生，…」算一願。兩版的偈皆為「起句＋當願眾生＋兩句願文」，每偈 4 個小句，已逐偈機器檢查，無例外。\n- 注意：六十華嚴 140 是本卷 CBETA 文字的客觀計數，不要在網頁上寫成 141；依上列十篇分段，兩版各篇偈數皆相同，只有「行腳」差 1（六十華嚴 57、八十華嚴 58），差異落在路上所見的景物與人（八十華嚴多「見無嚴飾」「見樂著人」「見無樂著」「見無病人」「見操行人」等，六十華嚴多「見素服人」「見志樂人」「見愁憂人」「見強健人」「若見仙人」等，兩版各自的條目不一一對應，確切是哪一條多出來待核）。\n')
L.append('## 三、十篇起訖（依偈序號 n）\n')
L.append('限制：規劃定稿文件（claude/來生出家簿-規劃定稿-2026-11-18.md）在 Projects 工具內，本次無法讀取，所以下列起訖是依偈文內容所擬，只有十篇名稱依任務所述。請與規劃定稿核對。\n')
for nm,doc in (('六十華嚴 T0278',a),('八十華嚴 T0279',b)):
    L.append('### '+nm+'\n')
    L.append('| 篇 | 偈序號 | 起句 | 末句 | 偈數 |\n|---|---|---|---|---|')
    for r in doc['ranges']:
        vs=[v for v in doc['verses'] if r['from'] and r['from']<=v['n']<=r['to']]
        L.append('| %s | %s–%s | %s | %s | %d |'%(r['section'],r['from'],r['to'],vs[0]['cond'],vs[-1]['cond'],len(vs)))
    L.append('')
L.append('十篇歸屬需特別核對的地方（待核）：\n')
L.append('- 待核：「手執錫杖」「擎持應器」歸「行腳」起點（兩版皆然）；若規劃定稿把錫杖、應器放在「威儀」或「乞食」，要改。')
L.append('- 待核：「行腳」篇含路上所見的樹、水、園林、各類人與城邑（六十華嚴 #47–#103；八十華嚴 #47–#104），內容龐雜，規劃定稿是否再細分未知。')
L.append('- 待核：「若入水時／澡浴身體／盛暑炎熾／隆寒氷結／諷誦經典」（六十華嚴 #126–#130 附近；八十華嚴對應「若入水時／洗浴身體／盛暑炎毒／暑退涼初／諷誦經時」）夾在「說法」與「禮佛」之間，暫歸「說法禮佛」，是否另屬威儀要核。')
L.append('- 待核：「若洗足時」暫歸「寢息」（兩版洗足皆在頂禮繞塔、讚佛之後、寢息之前）。')
L.append('- 待核：「若在聚會／若在危難」暫歸「在家」，而「以信捨家（六十）／捨居家時（八十）」為「捨家」起點。')
L.append('- 待核：「身／語／意」分類，CBETA 原文沒有標，我沒有自行分，JSON 的 section 欄只填十篇名稱。\n')
L.append('## 四、兩版差異（逐條列原文；格式：#偈序號 [CBETA 起行] 原文）\n')
for t,ca_,cb_ in items:
    L.append('### '+t+'\n')
    L.append('- 六十華嚴：'+fmt(a,ca_))
    L.append('- 八十華嚴：'+fmt(b,cb_)+'\n')
L.append('### 結構差異（起句只出現在一版的偈）\n')
L.append('- 只在六十華嚴（共 %d 偈）：'%len(only_a)+'、'.join(only_a)+'\n')
L.append('- 只在八十華嚴（共 %d 偈）：'%len(only_b)+'、'.join(only_b)+'\n')
L.append('以上以「起句」逐字比對；起句不同不代表內容無對應（譯語不同，如 受出家法／正出家時），只作為尋找差異的線索，不能當成對應表。\n')
L.append('## 五、版本校勘（CBETA 註，底本為大正藏）\n')
L.append('各偈的校勘註已放在 JSON 的 notes 欄（例：六十華嚴「除鬀」、「𦓷」、「憺怕」、「阬㵎」；八十華嚴「帬」、「妓」）。這些字網頁顯示時需確認字型。\n')
L.append('## 六、待核清單\n')
T=['十篇起訖：全部為依偈文內容初擬，未與規劃定稿核對（Projects 文件本次無法讀取）。',
'十篇內的細部歸屬：錫杖／應器、入水沐浴與寒暑、洗足、在聚會／在危難（見第三節）。',
'身／語／意分類：原文未標，未分。',
'intro 與 outro 的 CBETA 校勘註（如六十華嚴卷首問語中的 色／止／尸／禪 等）未逐條擷取，JSON 的 intro_notes_status 已註明。',
'逐字轉錄方式：Bash 連不到 CBETA，文字由雲端瀏覽器讀取 cbdata 回傳內容後以手工轉入檔案。已用 CBETA 全文檢索「當願眾生」的命中數（140、141）及行號交叉核對偈數，但「逐字」尚未做第二次獨立機器比對，建議抽查或在能連線的環境以 API 全卷重抓後 diff。',
'六十華嚴 140 偈對聖嚴法師 141 願：偈數差 1（見第二、四節），說法依據待核。',
'異體字顯示：𦓷（U+265F7）、憺怕、鬀、㵎、阬、麁歰（六十）／麁澁（八十）、帬，網頁字型需支援。',
'六十華嚴「遇難持戒／見捨戒人」與八十華嚴「見不捨人／見能捨人」是否為同一願的不同譯語，待核（只比對了起句，未比對義理）。']
for i,t in enumerate(T,1): L.append('%d. 待核：%s'%(i,t))
open(D+'check_report.md','w',encoding='utf-8').write('\n'.join(L)+'\n')
print('\n'.join(L)[:9000])
