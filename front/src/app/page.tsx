

import Image from "next/image";
import styles from "./page.module.css";
import Header from "./components/Header";
import Chatbot from "./components/Chatgpt";


export default function Home() {
  return (
    <main className={styles.main}>

    <Header></Header>
    <Chatbot></Chatbot>


    </main>
  );
}
