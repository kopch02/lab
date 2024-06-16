import { useEffect, useState } from 'react'
import s from './RunString.module.scss'

export const RunString = () => {

  const [displayText, setDisplayText] = useState('');
  const [speed, setSpeed] = useState(10)

  const handleFileChange = (e: { target: { files: any[]; }; }) => {
    const file = e.target.files[0]
    if (file) {
      const reader = new FileReader()
      reader.onload = () => {
        setDisplayText(reader.result)
      };
      reader.readAsText(file)
    }
  }




  const handleSpeedChange = (e: { target: { value: string; }; }) => {
    setSpeed(parseInt(e.target.value))
  }


  return (
    <div>
      <input type="file" accept=".txt" onChange={handleFileChange} />
      <input
        type="range"
        min="1"
        max="100"
        value={speed}
        onChange={handleSpeedChange}
      />
      <marquee behavior="scroll" direction="left" scrollamount={speed} height="50px" className={s.marq}>
        {displayText}
      </marquee>
    </div>
  )
}

