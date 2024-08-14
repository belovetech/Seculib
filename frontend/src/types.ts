export interface Book {
  id: string
  title: string
  author: string
  available: boolean
}

export interface BorrowedBook {
  book: {
    author: string
    id: string
    title: string
  }
  id: string
  book_id: string
  borrow_date: string
  return_date: string
  student_id: string
}

export interface User {
  id: number
  name: string
  matric_no: string
  department: string
  level: string
}

export interface State {
  user: User | null
}
