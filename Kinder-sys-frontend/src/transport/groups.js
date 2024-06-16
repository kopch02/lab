import { api } from "./api";

const groupsExtendedApi = api.injectEndpoints({
  endpoints: (build) => ({
    getGroups: build.query({
      query: () => `groups`,
    }),
  }),
});

export const { useGetGroupsQuery } = groupsExtendedApi;
