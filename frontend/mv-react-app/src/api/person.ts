import { makeRequest } from '@/api/base';
import type { Person } from '@/types/person';

const baseURL = 'http://localhost:8080/persons';

// TODO: call the get person endpoint
export async function getAllPersons(): Promise<Person[]> {
  return makeRequest<Person[]>(baseURL, 'GET');
};