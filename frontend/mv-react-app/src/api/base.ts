export async function makeRequest<T>(url: string, method: "GET" | "POST" | "PUT" | "DELETE", body?: any): Promise<T> {
  const response = await fetch(url, {
    method,
    headers: {
      "Content-Type": "application/json",
    },
    ...(body && { body: JSON.stringify(body) }),
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Request failed: ${response.status} ${response.statusText} - ${errorText}`);
  }

  return response.json() as Promise<T>;
}