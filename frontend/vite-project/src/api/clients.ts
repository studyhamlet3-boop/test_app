const BASE_URL = "http://127.0.0.1:8000";

export async function apiFetch( // either fetch or axios, but fetch is built-in
  endpoint: string,
  options: RequestInit = {},
  config = { redirectOnUnauthorized: true } /* default config */
) {
  const response = await fetch(`${BASE_URL}${endpoint}`, {
    ...options,

    credentials: "include", // send cookies automatically

    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
  });

  // backend says session invalid
  if (response.status === 409) {
    if (config.redirectOnUnauthorized) {
      window.location.href = "/register"; // force redirect to register page in case of cookie expire
    }
    throw new Error("Unauthorized: thrown by apiFetch");

  }

  return response;
}