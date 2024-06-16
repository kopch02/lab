import { diagnosticsReducer } from "./slices/diagnostics";
import { recommendationsReducer } from "./slices/recommendations";
import { statisticsReducer } from "./slices/statistics";
import { userReducer } from "./slices/user";

const reducers = {
  diagnosticsReducer,
  recommendationsReducer,
  userReducer,
  statisticsReducer,
};

export default reducers;
