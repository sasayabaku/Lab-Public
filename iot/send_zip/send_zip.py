import os
from datetime import datetime
import shutil

data_path = './dataDir'
zip_path = './zipfile'

if __name__ == '__main__':

    while True:

        # 現在時刻の取得
        now = datetime.now()

        # "0915"のように，現在の日付を文字列で取得
        nowStr = now.strftime("%m%d")

        # 画像があるディレクトリ一覧
        datalist = os.listdir(data_path)

        for dataDate in datalist:
            if nowStr != dataDate:

                # 圧縮対象のディレクトリのPATH
                targetDir = os.path.join(data_path, dataDate)
                # 圧縮先のzipファイルのPATH名
                saveZip = os.path.join(zip_path, dataDate)

                # その日の分を圧縮させてディレクトリを消す
                shutil.make_archive(saveZip, 'zip', root_dir=targetDir)
                shutil.rmtree(os.path.join(data_path, dataDate))

                # 新しい日付のディレクトリを作成
                os.mkdir(os.path.join(data_path, nowStr))
