# Focus Dice

カジノテイストの集中力アップアプリ

---

## 🚀 まずはアプリストアに公開するまでの手順

### 1. デベロッパーアカウントを用意
まずはそれぞれのアプリストアのデベロッパーアカウントを取得してください。
- **App Store**: Apple Developer Program（年間99ドル）
- **Google Play**: Google Play Console（1回限り25ドル）

---

### 2. パッケージのインストール
```bash
npm install
```

---

## 📱 iOS アプリをビルドして App Store に公開

#### 手順 1: iOSプラットフォームを追加
```bash
npm install @capacitor/ios
npx cap add ios
```

#### 手順 2: ビルドして同期
```bash
npm run ios:sync
```

#### 手順 3: Xcodeで開く
```bash
npm run ios:open
```

#### 手順 4: Xcodeで設定
1. プロジェクトナビゲータから `App` を選択
2. **Signing & Capabilities** タブで開発チームを選択
3. **Bundle Identifier** が `com.focusdice.app` になっているか確認
4. **Deployment Target** を iOS 14.0 以上に設定
5. **Signing Certificate** が有効になっているか確認

#### 手順 5: アイコンを設定
Xcodeの `Assets.xcassets` に以下のサイズのアイコンを追加してください。
- iPhone用: 1024x1024px, 60x60px@2x, 60x60px@3x
- iPad用: 76x76px, 76x76px@2x

#### 手順 6: Archive を作成
1. Xcode上部メニュー → **Product** → **Archive**
2. ビルドが完了したら Organizer ウィンドウが開きます
3. **Distribute App** ボタンをクリック
4. 「App Store Connect」を選択して手順に従う

#### 手順 7: App Store Connect で登録
1. https://appstoreconnect.apple.com にアクセス
2. 「マイアプリ → 「新しいApp」を作成
3. アプリ名、プライマリー言語、バンドルID（`com.focusdice.app`）、SKUを設定
4. スクリーンショット、説明、価格などの情報を入力
5. 審査情報を入力して審査に提出

---

## 🤖 Android アプリをビルドして Google Play に公開

#### 手順 1: Androidプラットフォームを追加
```bash
npm install @capacitor/android
npx cap add android
```

#### 手順 2: ビルドして同期
```bash
npm run android:sync
```

#### 手順 3: Android Studioで開く
```bash
npm run android:open
```

#### 手順 4: 署名キーストアを作成
1. Android Studio上部メニュー → **Build** → **Generate Signed App Bundle / APK**
2. 「Android App Bundle」を選択
3. 「Create new…」から新規キーストアを作成
4. パスワードとエイリアスを設定（大切に保管してください

#### 手順 5: アイコンを設定
`app/src/main/res/ 以下のディレクトリにアイコンを配置してください。
- mipmap-hdpi: 72x72px
- mipmap-mdpi: 48x48px
- mipmap-xhdpi: 96x96px
- mipmap-xxhdpi: 144x144px
- mipmap-xxxhdpi: 192x192px
- Google Playストア用: 512x512px

#### 手順 6: App Bundleをビルド
1. **Build** → **Generate Signed App Bundle / APK**
2. 先ほど作成したキーストアを選択してビルド
3. `app/release/app-release.aab` が出力されます

#### 手順 7: Google Play Console で登録
1. https://play.google.com/console にアクセス
2. 「Create Application」から新しいアプリを作成
3. アプリ名、デフォルト言語を設定
4. App Bundleをアップロード
5. スクリーンショット、説明、プライバシーポリシーなどの情報を入力
6. 審査情報を入力して審査に提出

---

## 📝 その他必要な情報

### アプリ情報のサンプル
- **アプリ名**: Focus Dice
- **簡単な説明: カジノテイストの集中力アップアプリ
- **詳細説明**: ダイスを振って集中時間を決めて、集中できたらギャンブルで遊べます。楽しみながら集中力を高めましょう。
- **スクリーンショット**: 実機で画面キャプチャして5枚程度用意
- **カテゴリ**: 仕事効率化, ツール
- **年齢レート**: 4+

---

## 🌐 PWAとして公開する方法（無料！）

PWAとして公開すると、スマホアプリのように使えて、App Store/Google Playに登録する必要はありません。

---

### 📦 事前準備
まずプロジェクトのgitリポジトリを作成しましょう。
```bash
git init
git add .
git commit -m "Initial commit"
```

**補足**: すでにファイルを`public`ディレクトリに移動しているので、そのままで大丈夫です！

---

### 方法1: Vercel（オススメ！）
Vercelは超簡単にPWAを公開できます。

#### 手順
1. https://vercel.com にアクセスしてGitHubアカウントでログイン
2. 「Add New → Project」を選択
3. 先ほど作成したFocus Diceのリポジトリを選択
4. 「Deploy」をクリック
5. 1分ほどで公開完了！

#### 使い方
- デプロイ後に表示されるURLにスマホでアクセス
- Safari/Chromeの「ホーム画面に追加」でアプリ化

---

### 方法2: Netlify
こちらも同じくらい簡単です。

#### 手順
1. https://netlify.com にアクセスしてGitHubアカウントでログイン
2. 「Add new site → Deploy with GitHub」を選択
3. Focus Diceのリポジトリを選択
4. 「Deploy site」をクリック

---

### 方法3: GitHub Pages
完全無料で使えますが、少し手順が多いです。

#### 手順
1. GitHubでリポジトリを作成
2. ローカルのコードをプッシュ
3. 「Settings → Pages」を開く
4. 「Branch」を main に、「Folder」を /root に設定
5. 「Save」をクリック
6. 2-3分で公開完了！

---

### ✨ PWAを使う方法

#### iOS（Safari）
1. 公開したURLをSafariで開く
2. 共有ボタンをタップ
3. 「ホーム画面に追加」をタップ
4. 「追加」をタップ

#### Android（Chrome）
1. 公開したURLをChromeで開く
2. メニュー（3点リーダー）をタップ
3. 「アプリをインストール」または「ホーム画面に追加」をタップ
4. 「追加」をタップ

---

## 🔐 Firebase ログイン & クラウド同期（オプション）

アプリにGoogleログイン機能とクラウドデータ同期機能を追加することができます。

### 1. Firebase プロジェクトを作成

1. [Firebase Console](https://console.firebase.google.com/) を開き、「**プロジェクトを作成**」をクリック
2. プロジェクト名を入力し、「**続行**」→「**プロジェクトを作成**」
3. プロジェクトが作成されたら、「**続行**」

### 2. ウェブアプリを登録

1. Firebase Console のトップページで、「**ウェブアプリを追加**」ボタン（`</>`アイコン）をクリック
2. アプリのニックネームを入力（例：`Focus Dice Web`）
3. 「**アプリを登録**」をクリック
4. 表示される「**const firebaseConfig = { ... }**」の部分をコピー

### 3. Firebase 設定ファイルを編集

1. プロジェクト内の `public/firebase-config.js` ファイルを開く
2. コピーした `firebaseConfig` の内容で、既存のダミーデータを置き換える

例：
```javascript
const firebaseConfig = {
  apiKey: "AIzaSy...", // 実際のAPIキー
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "1234567890",
  appId: "1:1234567890:web:abcdef123456"
};
```

### 4. Firebase サービスを有効化

#### Google ログインを有効化
1. Firebase Console の左メニューから「**Authentication**」を開く
2. 「**Sign-in method**」タブをクリック
3. 「**新しいプロバイダを追加**」→「**Google**」を選択
4. 「**有効にする**」をオン →「**保存**」

#### Firestore Database を作成
1. 左メニューから「**Firestore Database**」を開く
2. 「**データベースを作成**」をクリック
3. 「**テストモードで開始**」を選択 →「**次へ**」
4. ロケーションは「**asia-northeast1 (東京)**」を選択 →「**有効にする**」

### 5. デプロイ

設定が完了したら、変更を GitHub にプッシュすると Vercel が自動的に再デプロイします。

アプリを開くと、右上に「**Googleでログイン**」ボタンが表示されます！

---

## 📱 PWAとして使う
ウェブブラウザで `index.html` を開くか、HTTPSでホスティングしてホーム画面に追加してください。
