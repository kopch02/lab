import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { baseUrl } from "./config";

export const api = createApi({
  reducerPath: "kinderApi",
  baseQuery: fetchBaseQuery({ baseUrl }),
  endpoints: () => ({}),
});
