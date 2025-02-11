"use client"; // クライアントコンポーネントにする（`useState` を使うため）

import { useState, useEffect } from "react";

export default function Home() {
  const [message, setMessage] = useState("読み込み中..."); //useState() を使うと、その値を更新すると React が画面を再描画（レンダリング）してくれる

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => setMessage("エラーが発生しました"));
  }, []);

  return (
    <div
      style={{
        display: "flex",
        height: "100vh",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <h1 style={{ fontSize: "2rem", fontWeight: "bold" }}>{message}</h1>
    </div>
  );
}
