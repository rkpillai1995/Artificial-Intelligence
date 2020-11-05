/**
 *
 * __author__ = 'Rajkumar Pillai'
 *
 * file: hw3.pl
 * CSCI-630:  Found of Intelligent Systems
 * Author: Rajkumar Lenin Pillai
 *
 */


%!  %%%%%%%%%%%%%%%%% Male

male(george).
male(kydd).
male(philip).
male(charles).
male(mark).
male(andrew).
male(edward).
male(william).
male(harry).
male(peter).
male(beatrice).
male(james).

%!  %%%%%%%%%%%% female
female(mum).
female(spencer).
female(elizabeth).
female(margaret).
female(diana).
female(anne).
female(sarah).
female(sophie).
female(zara).
female(eugenie).
female(louise).


%!  %%%%%%%%%%% child relations

child(elizabeth,george).
child(elizabeth,mum).
child(margaret,george).
child(margaret,mum).

%!  %%%%%%%%%%%% child relations
%
child(diana,spencer).
child(diana,kydd).

child(charles,elizabeth).
child(charles,philip).

child(anne,elizabeth).
child(anne,philip).

child(andrew,elizabeth).
child(andrew,philip).

child(edward,elizabeth).
child(edward,philip).

%!  %%%%%%%%%% child relations

child(william,diana).
child(william,charles).
child(harry,diana).
child(harry,charles).


child(peter,anne).
child(peter,mark).
child(zara,anne).
child(zara,mark).

child(beatrice,andrew).
child(beatrice,sarah).
child(eugenie,andrew).
child(eugenie,sarah).

child(louise,edward).
child(louise,sophie).
child(james,edward).
child(james,sophie).


%!  %%%%%%%%% Spouse


spouse(mum,george).
spouse(spencer,kydd).
spouse(elizabeth,philip).
spouse(diana,charles).
spouse(anne,mark).
spouse(sarah,andrew).
spouse(sophie,edward).


%!  %%%%%%%%%% grandchild
grandchild(C,A):-
    child(C,B),child(B,A).


%!  %%%%%%%%%%%%%%% sibling
sibling(X,Y):-
   child(X,Z) ,child(Y,Z) ,X \= Y ,male(Z).

%!  %%%%%%%%%%%%%% brother
brother(X,Y) :-
    male(X),sibling(X,Y).


%!  %%%%%%%%%%%%%% sister
sister(X,Y) :-
    female(X),sibling(X,Y).


%!  %%%%%%%%%%%%%%%%%%% daughter
daughter(D,P):-
    female(D),child(D,P).

%!  %%%%%%%%%%%%%%%%%%%%%%% son
son(S,P):-male(S),child(S,P).

%!  %%%%%%%%%%%%%% first cousin
firstcousin(C,D) :-
    child(C,X) , child(D,Y) , sibling(X,Y).


%!  %%%%%%%%%%%%  brother in law
brotherinlaw(B,X):-
    spouse(X,M),brother(B,M).


%!  %%%%%%%%%%%%%%%%% sister in law
sisterinlaw(S,X):-
    spouse(X,M),sister(S,M).


%!  %%%%%%%%%%%%%%%%% Aunt
aunt(A,C):-
    child(C,P),(sister(A,P);sisterinlaw(A,P)).

%!  %%%%%%%%%%%%%%%%%%%% uncle
uncle(U,C):-
    child(C,P),(brother(A,P);brotherinlaw(A,P)).


%!  %%%%%%%%%%%%%% greatgrandparent
greatgrandparent(A,D):-
    child(D,C),child(C,B),child(B,A).

%!  %%%%%%%%%%%%%% ancestor
ancestor(A,X):-
    child(X,A);(child(B,A),ancestor(B,X)).

