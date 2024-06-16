import { Card, CardBody, Typography } from "@material-tailwind/react";

import s from "./Recommendation.module.scss";

const Recommendation = ({ category, high, mid, low }) => {
  return (
    <Card className={`mt-6 ${s.recommendation}`}>
      <CardBody>
        <Typography variant="h5" color="blue-gray" className="mb-2">
          {category}
        </Typography>
        <Typography className="my-4">
          Для высокого уровня рекомендуется сделать {high}
        </Typography>
        <Typography className="my-4">
          Для среднего уровня рекомендуется сделать {mid}
        </Typography>
        <Typography className="mt-2">
          Для низкого уровня рекомендуется сделать {low}
        </Typography>
      </CardBody>
    </Card>
  );
};

export default Recommendation;
