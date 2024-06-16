import { Card, Typography } from "@material-tailwind/react";
import s from "./Table.module.scss";
import useDiagnostics from "../../../viewmodel/hooks/diagnostics/useDiagnostics";

const TABLE_HEAD = ["№", "ФИО", "Начало года", "Конец  года"];

const Table = () => {
  const { diagnosticsData } = useDiagnostics();

  return (
    <Card className={`h-full w-full overflow-y-auto ${s.table}`}>
      <table className="w-full min-w-max table-auto text-left ">
        <caption className="border-b border-blue-gray-100 bg-blue-gray-100 p-3">
          {" "}
          Категория{" "}
        </caption>
        <thead>
          <tr>
            {TABLE_HEAD.map((head) => (
              <th
                key={head}
                className="border-b border-blue-gray-100 bg-blue-gray-50 p-4"
              >
                <Typography
                  variant="small"
                  color="blue-gray"
                  className="font-normal leading-none opacity-80"
                >
                  {head}
                </Typography>
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {diagnosticsData.map(({ childId, startScore, endScore }, index) => {
            const isLast = index === diagnosticsData.length - 1;
            const classes = isLast ? "p-4" : "p-4 border-b border-blue-gray-50";

            return (
              <tr key={childId} className="even:bg-blue-gray-50/50">
                <td className={classes}>
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="font-normal"
                  >
                    {`#${index + 1}`}
                  </Typography>
                </td>
                <td className={classes}>
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="font-normal"
                  >
                    {childId}
                  </Typography>
                </td>
                <td className={classes}>
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="font-normal"
                  >
                    {startScore}
                  </Typography>
                </td>
                <td className={classes}>
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="font-normal"
                  >
                    {endScore}
                  </Typography>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </Card>
  );
};

export default Table;
