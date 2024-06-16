import RecommendationsList from "../../components/recommendationsList/RecommendationsList";
import Table from "../../components/table/Table";
import Selection from "../../components/selection/Selection";
import { ChildrenForm } from "../../components/forms/ChildrenForm/ChildrenForm";
import { Stats } from "../../components/stats/Stats";

const EducatorPage = () => {
  return (
    <>
      <div className="flex flex-col gap-1">
        <div className="ml-auto mr-auto mt-2 flex-1">
          <Selection />
        </div>
        <div className="ml-auto mr-auto flex flex-row gap-10">
          <div className="flex flex-col gap-2">
            <div className="py-3">
              <Table />
              <ChildrenForm group="группа 1" />
            </div>
            <div className="py-3">
              <Stats start_data={start_data} end_data={end_data} />
            </div>
          </div>
          <div className="ml-auto mr-auto mt-2 flex-1">
            <RecommendationsList />
          </div>
        </div>
      </div>
    </>
  );
};




const start_data = [
  {
    count: 2,
    procent: "20%",
  },
  {
    count: 3,
    procent: "30%",
  },
  {
    count: 5,
    procent: "50%",
  },
];

const end_data = [
  {
    count: 0,
    procent: "0%",
  },
  {
    count: 1,
    procent: "10%",
  },
  {
    count: 9,
    procent: "90%",
  },
];
export default EducatorPage;
