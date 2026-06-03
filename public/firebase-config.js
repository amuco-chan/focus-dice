// ======================================
// ここにFirebaseの設定情報を入力してください！
// Firebase Console → プロジェクト設定 → マイアプリ → SDKの設定と構成 からコピー
// ======================================
const firebaseConfig = {
  apiKey: "ここにapiKeyを入力",
  authDomain: "ここにauthDomainを入力",
  projectId: "ここにprojectIdを入力",
  storageBucket: "ここにstorageBucketを入力",
  messagingSenderId: "ここにmessagingSenderIdを入力",
  appId: "ここにappIdを入力"
};

// Firebaseの初期化（自動的に実行されます）
if (typeof firebase !== 'undefined') {
  firebase.initializeApp(firebaseConfig);
}
