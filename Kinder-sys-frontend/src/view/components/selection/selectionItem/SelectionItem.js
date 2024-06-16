import { Select, Option } from "@material-tailwind/react";

export const SelectionItem = ({label, data}) => {
  return (
    <Select variant="standard" label={label}>
      {data.map((grop,index) => (
        <Option key={index}>{grop}</Option>
      ))}
    </Select>
  );
};
