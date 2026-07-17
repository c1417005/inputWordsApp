import { useState } from 'react'
import axios from 'axios'
import './App.css'


export const App = () => {
  const [data, setData] = useState("")

  const url = "http://127.0.0.1:8000";

  const GetData = () => {
    axios.get(url).then((res) => {
      setData(res.data);
    });
  };

  return (
    <>
      <div>
        <div>ここから処理</div>
        {data ? <div>{data.Hello}</div> : <button onClick={GetData}>データを取得</button>}
      </div>
    </>
  );
};


