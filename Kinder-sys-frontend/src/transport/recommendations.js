import { api } from "./api";

const recommendationExtendedApi = api.injectEndpoints({
  endpoints: (build) => ({
    getRecommendations: build.query({
      query: () => `recommendations`,
    }),
    getRecommendationsByCategoryId: build.query({
      query: (categoryId) => `recommendations/${categoryId}`,
    }),
    getRecommendationsByGroupId: build.query({
      query: (groupId) => `recommendations/${groupId}`,
    }),
    addRecommendation: build.mutation({
      query: (data) => ({
        url: "/recommendations",
        method: "POST",
        body: data,
      }),
    }),
    deleteRecommendation: build.query({
      query: (recommendationId) => `recommendations/${recommendationId}`,
    }),
  }),
});

export const {
  useGetRecommendationsQuery,
  useGetRecommendationsByCategoryIdQuery,
  useGetRecommendationsByGroupIdQuery,
  useAddRecommendationMutation,
  useDeleteRecommendationQuery,
} = recommendationExtendedApi;
