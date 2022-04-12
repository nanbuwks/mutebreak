# mutebreak

発話障害時に代わりに声を出してプレゼンを実現する支援システムです。

- IoTLT Vol. 43 での登壇などに使用しました。

# ファイル説明

- countandkick.py  カウントダウンと音楽再生
- readme このファイル
- superc.py OpenJTalkを使って入力した日本語を発話するPython3アプリ
- musics (Public Domain サンプルミュージックファイル)

# 使用方法

1. プレゼンファイルを全画面表示します。
2. あらかじめプレゼンファイルはPDF化しておくのがやりやすいようです。
3. ターミナルで superc.py を実行します。
4. ターミナルを最前面に配置、フォントサイズを大きくして見やすくし、プレゼンファイルの邪魔にならない最下部などに1行~2行表示できるようにします。
5. ターミナルに日本語文章を打ち込んで発話します。
6. プレゼンファイルをフォーカスを変更してページめくりします。
7. 必要に応じ、countandtick.py を併用します。

# 収録ミュージック

- Toreador_song_cleaned.ogg 
- カルメン 第1幕への前奏曲（闘牛士） ジョルジュ・ビゼー Performed by the Damrosch Orchestra in 1903. (2:28)
- ThreeMarchesMilitaires_Schubert.mp3 シューベルト,フランツ 軍隊行進曲第1番ニ長調 D.733-1,Op.51-1 Pヨーゼフ・ホフマン 1903年録音.mp3
