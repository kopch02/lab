import { useState } from "react";
import { SelectionItem } from "./selectionItem/SelectionItem";
import { MyButton } from "../button/MyButton";
import { GroupFrom } from "../forms/GroupForm/GroupFrom";
import useDiagnostics from "../../../viewmodel/hooks/diagnostics/useDiagnostics";

import s from "./Selection.module.scss";
import useUser from "../../../viewmodel/hooks/users/useUsers";

const GROUPS = ["Группа 1", "Группа 2", "Группа 3"];
const CATEGORIES = ["Категория 1", "Категория 2", "Категория 3"];

const Selection = () => {
  const [isActive, setIsActive] = useState(false);

  const toggleActive = () => {
    setIsActive(!isActive);
  };

  // const { diagnosticsData } = useDiagnostics();

  const { role } = useUser();

  return (
    <div className={s.selection}>
      <SelectionItem label={"Группа"} data={GROUPS} />
      {role === "admin" && <MyButton text="+" func={toggleActive} />}
      <GroupFrom isactive={isActive} toggleactive={toggleActive} />
      <SelectionItem label={"Категория"} data={CATEGORIES} />
      {role === "admin" && <MyButton text="+" func={toggleActive} />}
    </div>
  );
};

export default Selection;
