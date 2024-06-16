import React from "react";
import {
  Card,
  Input,
  Button,
  Typography,
  Select,
  Option,
} from "@material-tailwind/react";
import s from '../From.module.scss'

export const GroupFrom = ({isactive,toggleactive }) => {
  return (
    <div>
      <Card
        className={`${s.form_container} ${isactive ? s.active : ""}`}
        onClick={toggleactive}
      ></Card>
      <Card
        color="transparent"
        shadow={false}
        className={`${s.form} ${isactive ? s.active : ""}`}
      >
        <Typography variant="h4" color="blue-gray">
          Добавление новой группы
        </Typography>
        <Typography color="gray" className="mt-1 font-normal">
          Введите название группы
        </Typography>
        <form className="mb-2 mt-8 w-80 max-w-screen-lg sm:w-96">
          <div className="mb-1 flex flex-col gap-6">
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Название
            </Typography>
            <Input
              size="lg"
              placeholder="Название"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
            />
            {/* <Typography variant="h6" color="blue-gray" className="-mb-3">
          Группа
          </Typography>
          <Select
          className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
          >
            <Option/>
          </Select> */}
          </div>

          <Button className="mt-6" fullWidth>
            Добавить
          </Button>
        </form>
      </Card>
    </div>
  );
};
