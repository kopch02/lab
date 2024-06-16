import { api } from "./api";

const diagnosticsExtendedApi = api.injectEndpoints({
  endpoints: (build) => ({
    getDiagnosticsByGroupId: build.query({
      query: (groupId) => `diagnostics/${groupId}`,
    }),
    addDiagnosticsData: build.mutation({
      query: (data) => ({
        url: "/diagnostics",
        method: "POST",
        body: data,
      }),
    }),
  }),
});

export const {
  useGetDiagnosticsByGroupIdQuery,
  useAddDiagnosticsDataMutation,
} = diagnosticsExtendedApi;
