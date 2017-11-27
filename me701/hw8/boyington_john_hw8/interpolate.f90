program
    double precision :: x_new, x, y, v
    integer :: n, order
    x(1:3) = (/ 1, 2, 3 /)
    y(1:3) = (/ 2, 4, 6 /)
    
    v = interpolate(1.3, x, y, 3, 1)
    print *, v
end program

double precision function interpolate(x_new, x, y, n, order)
    double precision, intent(in) :: x_new
    double precision, dimension(:), intent(in) :: x, y
    integer, intent(in) :: n, order
    integer :: l=0, i=0, j=0, s=0, p=1
    integer ind(order+1)
    
    ! find points directly to left of x_new
    do i=0, n
        if(x_new .ge. x(i)) then
            l = i
            EXIT
        end if
    end do
    
    ! populate interpolation points
    do j=l, order+l+1
        ind(j-l) = j-((order+1)/2)
    end do
    
    ! shift interpolation points into existence if negative
    if (ind(0) .le. 0) then
        do i=0, order+1
            ind(i) = ind(i) +  0 - ind(0)
        end do
    end if
    
    ! shift interpolation points into existence if higher than n
    if (ind(order) .le. n-1) then
        do i=0, order+1
            ind(i) = ind(i) +  (n - 1) - ind(order)
        end do
    end if
    
    ! calculate Lagrange polynomials
    do i=0, order+1
        do j=0, order+1
            if(j .ne. i) then
                p = p * ((x_new - x(ind(j))) / (x(ind(i)) - x(ind(j))))
            end if
        end do
        s = s + (p * y(ind(i)));
        p = 1;
    end do
    interpolate = s
end function interpolate
