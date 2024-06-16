import React from 'react'

import s from './System.module.scss'

export const System = () => {
  return (
    <div className={s.container}>
      <ul className={s.book_list}>
        <li className={s.book_item}>
          <span className={s.book_name}>Война и мир</span>
          <span className={s.book_author}>Л. Н. Толстой</span>
          <span className={s.book_author}>Цена:300р</span>
          <button className={s.book_btn}>Взять книгу</button>
        </li>
        <li className={s.book_item}>
          <span className={s.book_name}>Мастер и маргарита</span>
          <span className={s.book_author}>М. А. Булгаков</span>
          <span className={s.book_author}>Цена:500р</span>
          <button className={s.book_btn}>Уведомить о наличии</button>
        </li>
      </ul>
    </div>
  )
}
