import { api } from "./api";

const categoriesExtendedApi = api.injectEndpoints({
  endpoints: (build) => ({
    getCategories: build.query({
      query: () => `categories`,
    }),
    addCategory: build.mutation({
      query: (data) => ({
        url: "/categories",
        method: "POST",
        body: data,
      }),
    }),
    deleteCategory: build.mutation({
      query: () => ({
        url: "/categories",
        method: "DELETE",
      }),
    }),
  }),
});

export const {
  useGetCategoriesQuery,
  useAddCategoryMutation,
  useDeleteCategoryMutation,
} = categoriesExtendedApi;
