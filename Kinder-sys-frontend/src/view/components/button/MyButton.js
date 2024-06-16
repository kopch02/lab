import { Button } from "@material-tailwind/react";

export const MyButton = ({ text, func }) => {
  return (
    <div className="flex w-max items-end gap-4 py-3">
      <Button size="md" onClick={func}>
        {text}
      </Button>
    </div>
  );
};
