import { useEffect, useState } from 'react'
import { getPassword } from '../../api/api';
import s from './Form.module.scss'

export const Form = () => {
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [correctPassword, setCorrectPassword] = useState('');

  useEffect(() => {
    const fetchPassword = async () => {
      try {
        const fetchedPassword = await getPassword();
        setCorrectPassword(fetchedPassword);
      } catch (error) {
        console.error('Ошибка получения пароля:', error);
        setErrorMessage('Произошла ошибка при получении пароля');
      }
    };

    fetchPassword();
  }, [])

  const handleChangePassword = (e) => {
    setPassword(e.target.value);
  };


  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(password)
    console.log(correctPassword)
    if (password == correctPassword) {
      setErrorMessage('');
    } else {
      setErrorMessage('Неверный пароль');
    }
  };
  return (
    <fieldset>
      <div className={`${s.lastName} ${s.input_container}`}>
        <span className={s.input_header}>Фамилия</span>
        <input
          type="text"
          className={`${s.name_input} ${s.input}`}
          placeholder="Фамилия"
          name="lastName"
        />
      </div>
      <div className={`${s.inicial} ${s.input_container}`}>
        <span className={s.input_header}>Инициалы</span>
        <input
          type="text"
          className={`${s.inicial_input} ${s.input}`}
          placeholder="Инициалы"
          name="inicial"
        />
      </div>
      <div className={`${s.password} ${s.input_container}`}>
        <span className={s.input_header}>Пароль</span>
        <input
          type="password"
          className={`${s.password_input} ${s.input}`}
          placeholder="Пароль"
          name="password"
          value={password}
          onChange={handleChangePassword}
        />
      </div>
      <span className={s.errorMessage}>{errorMessage}</span>
      <div className={`${s.count} ${s.input_container}`}>
        <span className={s.input_header}>Количество</span>
        <input
          type="number"
          className={`${s.count_input} ${s.input}`}
          placeholder="Количество"
          name="count"
        />
      </div>

      <div className={s.type}>
        <div className={`${s.type1} ${s.input_container}`}>
          <span className={s.input_header}>Тип</span>
          <select
            className={`${s.type1_select} ${s.select}`}
            name="type1_select"
          >
            <option>Куринные</option>
            <option>Свинные</option>
          </select>
        </div>
        <div className={`${s.type2} ${s.input_container}`}>
          <span className={s.input_header}>.</span>
          <select
            className={`${s.type1_select} ${s.select}`}
            name="type2_select"
          >
            <option>Отборные</option>
            <option>Помятые</option>
          </select>
        </div>
      </div>

      <div className={`${s.transport} ${s.input_header}`}>
        <div className={s.transport_item}>
          <input
            type="radio"
            id="mail"
            name="transport"
            value="mail"
          />
          <label htmlFor="mail">Почтой</label>
        </div>
        <div className={s.transport_item}>
          <input
            type="radio"
            id="electro"
            name="transport"
            value="electro"
          />
          <label htmlFor="electro">Электронно</label>
        </div>
        <div className={s.transport_item}>
          <input
            type="radio"
            id="courier"
            name="transport"
            value="courier"
          />
          <label htmlFor="courier">Курьером</label>
        </div>
      </div>

      <div className={s.naklodnay_check}>
        <span className={`${s.input_header} ${s.header_nakladnay}`}>
          Требуется накладная
        </span>
        <input
          type="checkbox"
          id="naklodnay_check"
          name="naklodnay_check"
          className={s.checkbox}
        />
        <label
          htmlFor="naklodnay_check"
          className={s.checkbox_label}
        ></label>
      </div>
      <div className={`${s.description} ${s.input_container}`}>
        <span className={s.input_header}>Дополнительная информация</span>
        <textarea
          className={`${s.description_input} ${s.input}`}
          placeholder="Дополнительная информация"
          name="description"
        />
      </div>
      <div className={s.btns}>
        <button
          className={s.form_btn}
          type="submit"
          onClick={handleSubmit}
        >
          Заказать
        </button>
        <button
          className={s.form_btn}
          type="reset"
        >
          Отменить
        </button>
      </div>
    </fieldset>
  )
}
