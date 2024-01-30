import create from 'zustand'

type Store = {
  ingredients: string[]
  add: (ingredient: string) => void
  remove: (ingredient: string) => void
}

export const useStore = create<Store>((set) => ({
  ingredients: [],
  add: (ingredient) => set((state) => ({ingredients: [...state.ingredients, ingredient]})),
  remove: (ingredient) => set((state) => state) //TODO: add removal to ingredient state store.
}))