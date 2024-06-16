import s from './ExploreAllArrow.module.scss'

export const ExploreAllArrow = () => {
  return (
    <div className={s.all_arrow}>
      <span>Explore All</span>
      <img
        src="img/arrow-line.svg"
        alt="arrow-line"
        className={s.arrow_line}
      />
      <img
        src="img/arrow-cursor.svg"
        alt="arrow-cursor"
        className={s.arrow_cursor}
      />
    </div>
  )
}
