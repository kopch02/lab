import { api } from "./api";

const statisticsExtendedApi = api.injectEndpoints({
  endpoints: (build) => ({
    getStatisticsByGroupIdAndYear: build.query({
      query: ({ groupId, year }) => `statistics/groups/${groupId}/years/${year}`,
    }),
  }),
});

export const { useGetStatisticsByGroupIdAndYearQuery } = statisticsExtendedApi;
