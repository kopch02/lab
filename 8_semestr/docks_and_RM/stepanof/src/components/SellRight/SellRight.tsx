import s from './SellRight.module.scss'

export const SellRight = () => {
  return (
    <div className={s.sell_right}>
      <div className={s.upload_file}>
        <div className={s.icon_container}>
          <img
            src="img/upload.svg"
            alt="upload"
            className={s.icon_container_img}
          />
          <span className={s.icon_container_span}>
            PNG, GIF, WEBP, MP4 or MP3. Max 1Gb.
          </span>
        </div>
        <input
          type="file"
          accept="image/*"
          className={s.input_file}
          name="file"
        />
      </div>
      <button className={s.upload_btn}>Upload</button>
    </div>
  )
}
