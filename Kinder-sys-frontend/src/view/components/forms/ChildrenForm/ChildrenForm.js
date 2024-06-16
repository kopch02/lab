import React from "react";
import {
  Card,
  Input,
  Button,
  Typography,
  Select,
  Option,
} from "@material-tailwind/react";

import { useState } from "react";
import { MyButton } from "../../button/MyButton";
import s from "../From.module.scss";
import useUser from "../../../../viewmodel/hooks/users/useUsers";

export const ChildrenForm = ({ group }) => {
  const [isActive, setIsActive] = useState(false);

  const toggleActive = () => {
    setIsActive(!isActive);
  };

  const { role } = useUser();
  return (
    <>
      {role === "admin" && <MyButton text="Добавить" func={toggleActive} />}
      <Card
        className={`${s.form_container} ${isActive ? s.active : ""}`}
        onClick={toggleActive}
      ></Card>
      <Card
        color="transparent"
        shadow={false}
        className={`${s.form} ${isActive ? s.active : ""}`}
      >
        <Typography variant="h4" color="blue-gray">
          Добавление ребёнка в {group}
        </Typography>
        <Typography color="gray" className="mt-1 font-normal">
          Введите фио и выберите группу для ребёнка
        </Typography>
        <form className="mb-2 mt-8 w-80 max-w-screen-lg sm:w-96">
          <div className="mb-1 flex flex-col gap-6">
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Фамилия
            </Typography>
            <Input
              size="lg"
              placeholder="Фамилия"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
            />
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Имя
            </Typography>
            <Input
              size="lg"
              placeholder="Имя"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
            />
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Отчество
            </Typography>
            <Input
              size="lg"
              placeholder="Отчество"
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
    </>
  );
};
