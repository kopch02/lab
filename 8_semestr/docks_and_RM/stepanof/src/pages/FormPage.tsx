import * as XLSX from 'xlsx';
import { useRef, useState } from 'react';

import s from './Form.module.scss';
import { Form } from '../components/Form/Form';
import { RunString } from '../components/RunString/RunString';

export const FormPage = () => {
  const formRef = useRef(null);
  const [formData, setFormData] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const form = formRef.current;
    const formDataEntries = new FormData(form).entries();
    const data = Array.from(formDataEntries).reduce((acc, [name, value]) => {
      acc[name] = value;
      return acc;
    }, {});
    setFormData([...formData, data]);
    form.reset();
  };

  const handleDownloadExcel = () => {
    const workbook = XLSX.utils.book_new();
    const worksheet = XLSX.utils.json_to_sheet(formData);
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Form Data');
    XLSX.writeFile(workbook, 'form_data.xlsx');
  };

  return (
    <>
      <section className="container">
        <RunString />
        <form
          className={s.form}
          ref={formRef}
          onSubmit={handleSubmit}
        >
          <h2 className={s.form_header}>ЗАО Птицефабрика №1</h2>
          <div className={s.form_container}>
            <Form />
            <button type="submit" className={s.form_btn}>Добавить в Excel</button>
            <button className={s.form_btn} onClick={handleDownloadExcel}>Скачать Excel</button>
          </div>
        </form>
      </section>
    </>
  );
};
