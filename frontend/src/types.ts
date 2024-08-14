export interface Book {
  id: string
  title: string
  author: string
  available: boolean
}

interface borrowedBookData {
  book: Omit<Book, 'available'>
  id: string
  book_id: string
  borrow_date: string
  return_date: string
  student_id: string
}

export interface BorrowedBook {
  borrowed_books: borrowedBookData[] | []
  count: number
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
  borrowedBooks: BorrowedBook
}
