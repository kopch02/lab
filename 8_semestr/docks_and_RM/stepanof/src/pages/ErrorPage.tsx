import s from './ErrorPage.module.scss'

export const ErrorPage = () => {
  return (
    <div className={s.error_page}>
      <img
        src="img/404.png"
        alt="Error 404 Page Not Found"
      />
      <a href="/">
        <button className={s.back_btn}>Back main</button>
      </a>
    </div>
  )
}
