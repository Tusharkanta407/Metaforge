export type SessionUser = {
  id: string;
  email: string;
  name?: string;
};

export async function getSessionUser(): Promise<SessionUser | null> {
  return null;
}
