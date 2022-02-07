create or replace function calculatecredithour
(salary in number)
is
zakatamount number;
begin
if salary < nisab then dbms.output_line('You are not eligible to pay zakat');
elsif salary > nisab then calculate zakat due;
dbms.output_line('The amount of zakat due is ' || zakatnumber);
end if;
end calculatecredithour;

create or replace function getstudfromsubj
(salary in number)
is
zakatamount number;
begin
if salary < nisab then dbms.output_line('You are not eligible to pay zakat');
elsif salary > nisab then calculate zakat due;
dbms.output_line('The amount of zakat due is ' || zakatnumber);
end if;
end getstudfromsubj;