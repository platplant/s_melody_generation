# Generation of a short piano melody
10秒程度のピアノメロディ生成のためのサンプルコードです。Transformerを利用

Google Colaboratoryにs_melody_generation.ipynbと、それぞれのファイルをアップロードすることで実行ができます。
### 楽曲二値分類学習済みモデル(model_cpu.pth, model_gpu.pth)
213曲のピアノ楽曲データを用いて学習を行ったモデルです。
### メロディ生成手法
良いメロディ悪いメロディの二値分類を行うモデルを作成し(楽曲二値分類学習済みモデル)、ランダム入力データのメロディに対して、二値分類モデルがより良いメロディと判断するようにトークンの変更を繰り返すことで、良いメロディを生成します。
### メロディ生成例(成功例)



https://github.com/platplant/s_melody_generation/assets/157796397/e3d581aa-d3f5-4065-a118-06d23f5f8317



https://github.com/platplant/s_melody_generation/assets/157796397/e71de1c2-ffac-4595-b646-edc93fefc422



https://github.com/platplant/s_melody_generation/assets/157796397/846e9f5d-c88c-489f-8b05-1c6efe51291b



https://github.com/platplant/s_melody_generation/assets/157796397/e10a2e75-3c58-4280-8e49-d03f6691d91c



https://github.com/platplant/s_melody_generation/assets/157796397/bcbb5380-91e4-4f40-9fc2-ed5c74291fa2


### メロディ生成例(平均的な生成例)



https://github.com/platplant/s_melody_generation/assets/157796397/30a1a133-ede5-4f9c-b4c7-795d95aa90bf



https://github.com/platplant/s_melody_generation/assets/157796397/7f5136ce-81b1-4031-a268-15d2c5fcfa45



https://github.com/platplant/s_melody_generation/assets/157796397/0d405e38-8399-4b10-90a4-022db46d64e9



https://github.com/platplant/s_melody_generation/assets/157796397/73064660-fc7a-44dc-82d2-e283c50b74c1



https://github.com/platplant/s_melody_generation/assets/157796397/656efc11-fddd-4d49-897c-620363e2ac62

### 今後
主旋律(歌詞を声に出して歌うメロディパート・副旋律声部)と、副旋律が213曲のピアノ楽曲データにはあるが、同じ高さのものは同じトークンと認識しているため、それぞれ独立したトークンに変更する。

現段階では、主旋律と副旋律が混ざったものが生成されている。また、テンポ120のものしか生成できないため改良したい。
